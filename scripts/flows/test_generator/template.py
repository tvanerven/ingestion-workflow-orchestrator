STANDARD_TEMPLATE = {
    "datasetVersion": {
      "license": {
        "name": "CC BY 4.0",
        "uri": "http://creativecommons.org/licenses/by/4.0"
      },
      "metadataBlocks": {
        "citation": {
          "displayName": "Citation Metadata",
          "name": "citation",
          "fields": [
            {
              "typeName": "title",
              "multiple": False,
              "typeClass": "primitive",
              "value": ""
            },
            {
              "typeName": "alternativeURL",
              "multiple": False,
              "typeClass": "primitive",
              "value": ""
            },
            {
              "typeName": "otherId",
              "multiple": True,
              "typeClass": "compound",
              "value": [
                {
                  "otherIdAgency": {
                    "typeName": "otherIdAgency",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": "Zenodo"
                  },
                  "otherIdValue": {
                    "typeName": "otherIdValue",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  }
                }
              ]
            },
            {
              "typeName": "alternativeTitle",
              "multiple": True,
              "typeCfalselass": "primitive",
              "value": []
            },
            {
              "typeName": "dsDescription",
              "multiple": True,
              "typeClass": "compound",
              "value": [
                {
                  "dsDescriptionValue": {
                    "typeName": "dsDescriptionValue",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  }
                }
              ]
            },
            {
              "typeNamfalsee": "keyword",
              "multiple": True,
              "typeClass": "compound",
              "value": [
                {
                  "keywordValue": {
                    "typeName": "keywordValue",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  }
                }
              ]
            },
            {
              "typeName": "author",
              "multiple": True,
              "typeClass": "compound",
              "value": [
                {
                  "authorName": {
                    "typeName": "authorName",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  },
                  "authorAffiliation": {
                    "typeName": "authorAffiliation",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  },
                  "authorIdentifierScheme": {
                    "typeName": "authorIdentifierScheme",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  },
                  "authorIdentifier": {
                    "typeName": "authorIdentifier",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  }
                }
              ]
            },
            {
              "typeName": "datasetContact",
              "multiple": True,
              "typeClass": "compound",
              "value": [
                {
                  "datasetContactEmail": {
                    "typeName": "datasetContactEmail",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": "info@sharemusic.se"
                  }
                }
              ]
            },
            {
              "typeName": "subject",
              "multiple": True,
              "typeClass": "controlledVocabulary",
              "value": [
                "Arts and Humanities"
              ]
            },
            {
              "typeName": "distributionDate",
              "multiple": False,
              "typeClass": "primitive",
              "value": ""
            },
            {
              "typeName": "timePeriodCovered",
              "multiple": True,
              "typeClass": "compound",
              "value": [
                {
                  "timePeriodCoveredStart": {
                    "typeName": "timePeriodCoveredStart",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  },
                  "timePeriodCoveredEnd": {
                    "typeName": "timePeriodCoveredEnd",
                    "multiple": False,
                    "typeClass": "primitive",
                    "value": ""
                  }
                }
              ]
            }
          ]
        },
        "FAIRVaultCustomMetadata": {
          "displayName": "FAIRVault Custom metadata",
          "name": "FAIRVaultCustomMetadata",
          "fields": [
            {
              "typeName": "FVAccessConditions",
              "multiple": False,
              "typeClass": "compound",
              "value": {
                "FVAccessRights": {
                  "typeName": "FVAccessRights",
                  "multiple": False,
                  "typeClass": "primitive",
                  "value": "Green"
                }
              }
            }
          ]
        }
      }
    }
  }