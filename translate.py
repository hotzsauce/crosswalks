"""
translate the crosswalks here into dictionaries that are interpretable by
a FunnelMap
"""

from __future__ import annotations

import json

measures = ['quantity', 'price', 'nominal', 'real']


def sniff_sources(cross_map: dict) -> list:
	"""
	grab all the source names

	Parameters
	----------
	cross : dct
		the unaltered crosswalk dictionary
	"""

	first_cross = list(cross_map.values())[0]
	measure_maps = first_cross[measures[0]]

	return list(measure_maps.keys())

def ensure_hashable(obj):
	"""make sure mappings & iterables are hashable """
	try:
		vals = obj.values()
		return tuple(vals)

	except AttributeError:

		if isinstance(obj, str):
			return obj

		return tuple(obj)



def translate(
	obj: Union[str, dict],
	source: str = 'edan',
	as_funnel: bool = False,
	strict: bool = True
) -> Union[dict, FunnelMap]:
	"""
	translate the stored crosswalk-type jsons stored here into (1) dictionaries
	that could be read into a FunnelMap with no alterations, or (2) a FunnelMap
	directly.

	Parameters
	----------
	obj : str | dict
		a string or path-like object to the json, or an already-read-in
		crosswalk dictionary
	source: str ( = 'edan' )
		the data source to make the id of the FunnelMap
	as_funnel : bool ( = False )
		if False, return a dictionary. if True, return a FunnelMap with the
		dictionary as the underlying mapping. the `funnelmap` package is required
	strict : bool ( = True )
		no effect if `as_funnel = False`. otherwise, in the case of duplicate
		aliases, determines if a KeyError should be raised upon FunnelMap
		initialization. if `strict = False`, no error is raised and the mapping
		to the first id is preserved

	Returns
	-------
	dict | FunnelMap
	"""
	try:
		with open(obj, 'r') as json_file:
			cross_map = json.load(json_file)
	except TypeError:
		cross_map = obj

	# the api sources in this crosswalk dictionary
	aliases = sniff_sources(cross_map)

	# ensure this 'id' is in the sources
	if source not in aliases:
		raise ValueError(f"{repr(source)} is not in this crosswalk") from None

	funnel_dict = {}
	for cross in cross_map.values():

		for measure in measures:
			try:
				# some series are not quantity or price indices, or nominal
				meas_sources = cross[measure]

				id_ = ensure_hashable(meas_sources.pop(source))
				aliases = [ensure_hashable(v) for v in meas_sources.values()]

				if len(aliases) == 1:
					funnel_dict[id_] = aliases[0]
				else:
					funnel_dict[id_] = aliases
			except KeyError:
				pass

	if as_funnel:
		try:
			import funnelmap
		except ModuleNotFoundError:
			raise ModuleNotFoundError(
				"'funnelmap' library is needed if `as_funnel = True`"
			) from None

		return funnelmap.FunnelMap(funnel_dict, strict)

	return funnel_dict
