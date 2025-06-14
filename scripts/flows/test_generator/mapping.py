STANDART_MAPPING = {
    "title": ["title"],
    "author": {
        "mapping": "authors[*]",
        "children": {
            "authorName": ["name"],
            "authorAffiliation": ["affiliation"],
            "identifierScheme": ["identifier_scheme"],
            "identifier": ["identifier"]
        }
    },
    "datasetContact": {
        "mapping": "dataset_contacts[*]",
        "children": {
            "datasetContactName": ["name"],
            "datasetContactAffiliation": ["affiliation"],
            "datasetContactEmail": ["email"],
        }
    },
    "otherIdValue": ["doi"],
    "dsDescriptionValue": ["description"],
    "keywordValue": ["keywords[*]"],
    "language": ["language"],
    "alternativeURL": ["alternative_url"],
    "timePeriodCoveredStart": ["start_date"],
    "timePeriodCoveredEnd": ["end_date"],
    "subject": ["subject"],
}