# دیکشنری بخش‌های دستگاه
device_sections_map = {
    'ES & SCADA': {
        'RECTIFIRE': {
            'numeric_fields': {
                'LOAD VOLT': {'unit': 'V', 'range': (200, 250)},
                'INPUT VOLT': {'unit': 'V', 'range': (180, 240)}
            },
            'option_fields': {
                'CHARGER STATUS': {
                    'options': ['A/I', 'A/B', 'A/C'],
                    'normal': 'A/I'
                },
                'FAULT&ALARM': {
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'
                }
            }
        },
        'BUA01': {
            'numeric_fields': {
                'INC. 1 VOLT': {'unit': 'V', 'range': (210, 230)},
                'BUS-BAR 1 VOLT': {'unit': 'V', 'range': (210, 230)},
                'BUS-BAR 1 CURR': {'unit': 'A', 'range': (0, 100)},
                'INC. 2 CURR': {'unit': 'A', 'range': (0, 100)},
                'SELECTOR PANEL': {'unit': '', 'range': None}
            },
            'option_fields': {
                'POWER SUPPLY': {
                    'options': ['l', 'j', 'k'],
                    'normal': 'l'
                } 
            }
        }
    },
    'DG': {
        'DG1': {
            'numeric_fields': {
                'Battery voltage': {'unit': 'V', 'range': (26, 28)},
                'coolant temp': {'unit': '°C', 'range': (34, 100)}
            }, 
            'option_fields': {
                'level of fuel': {
                    'options': ['ok', 'Not ok'], 
                    'normal': 'ok'
                },
                'Leakage': {
                    'options': ['ok', 'Not ok'], 
                    'normal': 'ok'
                },
                'DG mode(Local panel)': {
                    'options': ['Auto', 'Manual'], 
                    'normal': 'Auto'
                },
                'DG mode(8610)': {
                    'options': ['Auto', 'Manual'], 
                    'normal': 'Auto'
                }
            }
        },
        'DG2': {
            'numeric_fields': {
                'Battery voltage': {'unit': 'V', 'range': (26, 28)},
                'coolant temp': {'unit': '°C', 'range': (34, 100)}
            }, 
            'option_fields': {
                'level of fuel': {
                    'options': ['ok', 'Not ok'], 
                    'normal': 'ok'
                },
                'Leakage': {
                    'options': ['ok', 'Not ok'], 
                    'normal': 'ok'
                },
                'DG mode(Local panel)': {
                    'options': ['Auto', 'Manual'], 
                    'normal': 'Auto'
                },
                'DG mode(8610)': {
                    'options': ['Auto', 'Manual'], 
                    'normal': 'Auto'
                }
            }
        }
    },
    'Battery': {
        'Set1': {
            'numeric_fields': {
                'Battery voltage -set1': {'unit': 'V', 'range': ()},
                'Battery current-set1': {'unit': 'A', 'range': ()}
            }
        },
        'Set2': {
            'numeric_fields': {
                'Battery voltage -set2': {'unit': 'V', 'range': ()},
                'Battery current-set2': {'unit': 'A', 'range': ()}
            }
        },
        'Room': {
            'numeric_fields': {
                'Temp': {'unit': '°C', 'range': ()}
            },
            'option_fields': {
                'ventilaton fan is in service': {
                    'options': ['ok', 'Not ok'], 
                    'normal': 'ok'
                },
                'Battery sulphated': {
                    'options': ['ok', 'Not ok'], 
                    'normal': 'ok'
                },
                'Level of water': {
                    'options': ['ok', 'Not ok'], 
                    'normal': 'ok'
                }
            }
        }
    }
}