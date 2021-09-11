sample_data = {
    "role": [{
        "roleType":
        "beneficiaryCustomer",
        "party": [{
            "partyType":
            "individual",
            "account": [{
                "network": "swift",
                "institutionName": "Westpac Banking Corporation",
                "institutionCode": "WBC",
                "country": "AU",
                "branchId": "733-750",
                "branchName": "Wangaratta",
                "streetAddress": "98 Murphy Street",
                "postcode": "3677",
                "suburb": "Wangaratta",
                "state": "VIC",
                "number": "063015189"
            }],
            "name": [{
                "fullName": "DAISEY TRIMUEL"
            }],
            "gender":
            "MALE",
            "identification": [{
                "identificationType": "benefitsCard",
                "identifier": "22417129951"
            }],
            "jobTitle":
            "Unemployed",
            "address": [{
                "suburb": "Wangaratta",
                "streetAddress": "1 Steane Street",
                "postcode": "3677",
                "state": "VIC",
                "country": "AU",
                "geolocation": {
                    "lon": "146.3088965",
                    "lat": "-36.3563499"
                }
            }],
            "partyId":
            "dcf06b5b29c3e950e392d6b5f26d3003e8c84c8fed79edf9edf07d9be6c15d5b",
            "consolidatedPartyId":
            "293283256248a98e52bd86aa85b77e13cee9bf38db13ab28d967ecd680bde941"
        }]
    }, {
        "roleType":
        "orderingCustomer",
        "party": [{
            "partyType":
            "individual",
            "account": [{
                "network": "swift",
                "branchName": "BANCO MILLENNIUM ATLANTICO, S.A.",
                "country": "AO",
                "suburb": "Luanda",
                "branchId": "PRTLAOLU",
                "number": "165993405"
            }],
            "name": [{
                "fullName": "Mrs M ACEDO"
            }],
            "gender":
            "FEMALE",
            "identification": [{
                "identificationType": "benefitsCard",
                "identifier": "2241712983951"
            }],
            "address": [{
                "suburb": "Chela",
                "postcode": "",
                "state": "",
                "country": "AO",
                "geolocation": {
                    "lon": "15.43358",
                    "lat": "-12.30261"
                }
            }],
            "partyId":
            "9b399e47b71d50fa2978fa18a316278e8b3ff6693e238f4184636a977dd44eeb",
            "consolidatedPartyId":
            "f6add6b65ff284fb27588e4188a2f60233fa41cce34cadca484196684b310c01"
        }]
    }],
    "transaction": {
        "direction": "incoming",
        "reference": "0100438011944",
        "amount": "138973.64",
        "transactionDatetime": "2020-04-10T09:08:08+1000"
    },
    "report": {
        "reportNumber": 595146553746,
        "reportType": "internationalFundsTransferInstruction",
        "reporter": "Westpac Banking Corporation",
        "reporterId": "45430",
        "processedDatetime": "2020-04-11T04:33:30+1000",
        "submissionId": "45430-20200411-001"
    }
}

transaction_report_mapping = {
    "index_patterns": ["transaction-report"],
    "template" : {
    "settings": {
        "number_of_shards": 3,
        "number_of_replicas": 0,
        "index.codec": "best_compression",
        "index.refresh_interval": "30s",
        "index.max_result_window": 20000,
        #"sort.field": "report.processedDatetime",
        #"sort.order": "asc",
        "analysis": {
            "analyzer": {
                "account_number_analyzer": {
                    "tokenizer": "standard",
                    "char_filter": ["account_number_filter"]
                }
            },
            "char_filter": {
                "account_number_filter": {
                    "type": "pattern_replace",
                    "pattern": "[^0-9]",
                    "replacement": ""
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "role": {
                "type": "nested",
                "properties": {
                    "party": {
                        "type": "nested",
                        "properties": {
                            "account": {
                                "type": "nested",
                                "properties": {
                                    "branchName": {
                                        "type": "text",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "branchId": {
                                        "type": "text",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "country": {
                                        "type": "text",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "network": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "number": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "analyzer": "account_number_analyzer",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "postcode": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "state": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "streetAddress": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "suburb": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    }
                                }
                            },
                            "address": {
                                "type": "nested",
                                "properties": {
                                    "country": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "geolocation": {
                                        "type": "geo_point"
                                    },
                                    "postcode": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "state": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "streetAddress": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "suburb": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    }
                                }
                            },
                            "gender": {
                                "type": "text",
                                "copy_to": "all",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "identification": {
                                "type": "nested",
                                "properties": {
                                    "identifier": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "identificationType": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    },
                                    "identificationSubType": {
                                        "type": "text",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    }
                                }
                            },
                            "jobTitle": {
                                "type": "text",
                                "copy_to": "all",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "name": {
                                "type": "nested",
                                "properties": {
                                    "fullName": {
                                        "type": "text",
                                        "copy_to": "all",
                                        "fields": {
                                            "keyword": {
                                                "type": "keyword",
                                                "ignore_above": 256
                                            }
                                        }
                                    }
                                }
                            },
                            "partyId": {
                                "type": "text",
                                "copy_to": "all",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            },
                            "partyType": {
                                "type": "text",
                                "copy_to": "all",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                }
                            }
                        }
                    },
                    "roleType": {
                        "type": "text",
                        "copy_to": "all",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    }
                }
            },
            "transaction": {
                "properties": {
                    "amount": {
                        "type": "double"
                    },
                    "direction": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "transactionDatetime": {
                        "type":
                        "date",
                        "format":
                        "yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd||strict_date_optional_time"
                    }
                }
            },
            "report": {
                "properties": {
                    "processedDatetime": {
                        "type":
                        "date",
                        "format":
                        "yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd||strict_date_optional_time"
                    },
                    "reportNumber": {
                        "type": "long"
                    },
                    "reportType": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "reporter": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "reporterId": {
                        "type": "integer",
                    },
                    "submissionId": {
                        "type": "keyword",
                    }
                }
            },
            "all": {
                "type": "text"
            }
        }
    }}
}