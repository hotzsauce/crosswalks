# crosswalks

Various crosswalks I've found convenient to store. Mostly concerning BEA underlying tables & my personal project, `edan`, and BEA-FRED correspondences.

---

### edan-bea\_underlying\_pce.json

Stores the underlying PCE series codes in BEA tables `2.4.3U`, `2.4.4U`, `2.4.5U`, `2.4.6U`; corresponding to quantity index, price index, nominal consumption, and real consumption series, respectively. Those table names and series codes are mapped to the unique codes used in the `edan` library, and other nice-to-have data (full name, table row, etc.) are stored.

### edan-bea-fred\_gdp.json

Stores the basic GDP series codes in BEA tables `1.1.3`, `1.1.4`, `1.1.5`, `1.1.6`; corresponding to quantity index, price index, nominal compensation, and real consumption series, respectively. Those table names and series codes are mapped to the unique codes used in the `edan` library, the FRED codes, and other nice-to-have data (full name, table row, etc.) are stored.


### edan-bea-fred\_gdp\_.json

Stores the detailed GDP series codes in BEA tables `1.5.3`, `1.5.4`, `1.5.5`, `1.5.6`; corresponding to quantity index, price index, nominal compensation, and real consumption series, respectively. Those table names and series codes are mapped to the unique codes used in the `edan` library, the FRED codes, and other nice-to-have data (full name, table row, etc.) are stored.


## Notes

The BEA API needs separate `table_name` and `series_code` parameters to retrieve the correct series. Rather than store these as separate entries, these identifiers are concatenated with a `!` used as a delimiter, so a single string can be used.
