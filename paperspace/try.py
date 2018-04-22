#!/usr/bin/env python3
with wget.download(http://www.patentsview.org/data/20171226/cpc_current.tsv.zip) as file:
    with ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall()