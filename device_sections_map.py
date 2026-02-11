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
    'Battery ': {
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
    },
    'LV EMERGENCY BUS BAR':{
        'BMC BUS BAR':{

            'numeric_fields':{
                
                'Incoming 1 Voltage(BHA)' : {'unit' : 'V', 'range':(380 , 420)},
                'Incoming 2 Voltage(BMA)' : {'unit' : 'V', 'range':(380 , 420)}
            } ,
            'option_fields':{
                'AUTO/MANUAL Selector' : {
                    'options': ['Auto', 'Manual'], 
                    'normal': 'Auto'},
                'Energized From INCOMING 1/2':{
                    'options':['1', '2']
                }    
            }
                       },

        'LV EMERGENCY BUS BAR BMA / BMB':{
             'numeric_fields':{
                 'BMA incoming voltage'  :{'unit' : 'V', 'range':(380, 420)},
                 'BMA bus voltage'  :{'unit' : 'V', 'range':(380, 421)},
                 'BMA incoming current'  :{'unit' : 'A', 'range':None},
                 'BMB incoming voltage'  :{'unit' : 'V', 'range':(380, 420)},
                 'BMB BUS voltage'  :{'unit' : 'V', 'range':(3)},
                 'BMB incoming current'  :{'unit' : 'A', 'range':None}

             },
             'option_fields' :{
                 'incoming from BHA':{
                     'options': ['Open', 'Close'], 
                    'normal': 'Open'
                 },
                 'Incom. From BHB':{
                     'options': ['Open', 'Close'], 
                    'normal': 'Open'
                 },
                 'LOCAL/REMOTE Selector':{
                     'options': ['LOCAL', 'REMOTE'], 
                    'normal': 'REMOTE'
                 },
                 'Fault and alarm':{
                     'options': ['OK', 'NOTOK'], 
                    'normal': 'OK'
                 }
             }

        }

    },
    'SLIP RING':{
        'SLIP RING':{
              'option_fields':{
                  'SLIP RING( NOISE)':{
                      'options' : ['OK'  , 'NOT OK'],
                      'normal' : 'OK'
                  },
                  'BRUSHES FLEXIBLE CONNECTION':{
                      'options' : ['OK'  , 'NOT OK'],
                      'normal' : 'OK'
                  },
                  'SLIP RING( CLEANING)':{
                      'options' : ['OK'  , 'NOT OK'],
                      'normal' : 'OK'
                  },
                  'SLIP RING( ARC)':{
                      'options' : ['OK'  , 'NOT OK'],
                      'normal' : 'OK'
                  }
                  
              }
        }
    },
    'LUBE OIL SKID':{
        'LUBE OIL SKID':{
            'numeric_fields':{
                'Main Lube Oil Pump Disch. Press':{'unit' :'bar', 'range':(5.5, None)},
                'Lube Oil Filter ΔP':{'unit' :'z', 'range':(None,40)},
                'Lube Oil Press After Filter':{'unit' :'bar', 'range':(1.7, None)},
                'Lube Oil Tank Vacuum press.':{'unit' :'mbar','range':(-6.5 , -5.5)},
                'Lube Oil Filter In Service':{'unit' :'1/2'},
                'GT Jacking Discharge Press.':{'unit' :'bar','range':(150, None)},
                'Gen Jacking Discharge Press.':{'unit' :'bar','range':(250, None)},
                'Comp. Bear jack. Press.':{'unit' :'bar','range':(90 , 100)},
                'GT. Bear Jack. Press':{'unit' :'bar','range':(90 , 100)},
                'Gen. CE Bear Jack. Press':{'unit' :'bar','range':(90 , 100)},
                'Gen. OCE Bear Jack. Press':{'unit' :'bar','range':(90 , 100)},
                'Lube Oil Tank Temp':{'unit' :'ºc','range':(35, 75)}
            },
            'option_fields':{
                'Lube Oil Tank Level':{
                        'options':['Low', 'Normal' , 'High'] ,
                        'normal' : 'Normal'
                },
                'Sound Of Motors':{
                        'options':['Low', 'Normal' , 'High'] ,
                        'normal' : 'Normal'
                },
                'Leakage And Cleaning':{
                        'options' : ['OK'  , 'NOT OK'],
                        'normal' : 'OK'
                }
            }

        },

        'LUBE OIL COOLER':{
                 'numeric_fields':{
                     'Cooler In Service':{'unit' :'1/2'},
                     'Lube Oil Inlet Temp.':{'unit' :'ºc', 'range':(60,70)},
                     'Lube Oil Inlet Press.':{'unit' :'bar', 'range':(5,6)},
                     'Lube Oil Outlet Temp.':{'unit' :'ºc', 'range':(15,48)},
                     'Lube Oil Outlet Press.':{'unit' :'bar', 'range':(4,6)},
                     'Water Inlet Cooler Temp.':{'unit' :'ºc'},
                     'Water Inlet Cooler Press.':{'unit' :'bar', 'range':(3)},
                     'Water Outlet Cooler Temp.':{'unit' :'ºc'},
                     'Water Outlet Cooler Press.':{'unit' :'bar', 'range':(1.8, 2.2)}
                 },
                  'option_fields':{
                      'Leakage':{
                        'options' : ['OK'  , 'NOT OK'],
                        'normal' : 'OK'
                      }
                  }

        }
    },
    'ROOM':{
        'SCADA':{
             'numeric_fields':{
                 'ROOM TEMPERATURE':{'unit':'°C' , 'range':(22,24)},
                 'BUS-BAR TEMPERATURE':{'unit':'°C' , 'range':(22,24)},
             }
        },
        'ES':{
            'numeric_fields':{
               'ROOM TEMPERATURE':{'unit':'°C' , 'range':(22,24)},
            }
        },
        'CCR':{
            'numeric_fields':{
                'ROOM TEMPERATURE':{'unit':'°C' , 'range':(22,24)},
            }
        }
    },
    'CUN-P 01':{
        'RECTIFIRE 400VAC/52VDC':{
             'numeric_fields':{
                 'LOAD VOLT 1.':{'unit': 'V'},
                 'INPUT VOLT 1.':{'unit': 'V'},
                 'LOAD VOLT 2.':{'unit': 'V'},
                 'INPUT VOLT 2.':{'unit': 'V'}
             },
             'option_fields':{
                 'CHARGER STATUS 1':{
                     'options':['I', 'B' , 'F']
                 },
                 'FAULT & ALARM 1':{
                     'options':['OK'  , 'NOT OK']
                 },
                 'CHARGER STATUS 2':{
                     'options':['I', 'B' , 'F']
                 },
                 'FAULT & ALARM 2':{
                     'options':['OK'  , 'NOT OK']
                 }
             }


        },
        'BUA01':{
            'numeric_fields':{
                 'INC. 1  VOLT.':{'unit': 'V'},
                 'BUS-BAR 1 VOLT.':{'unit': 'V'},
                 'BUS-BAR 1 CURR.':{'unit': 'A'},
                 'INC. 2  VOLT.':{'unit': 'V'},
                 'BUS-BAR 2 VOLT.':{'unit': 'V'},
                 'BUS-BAR 2 CURR.':{'unit': 'A'}
             },
             'option_fields':{
                 'SELECTOR PANEL':{
                     'options': ['Auto', 'Manual']
                     
                 }
             }


        },
        'CUN01':{
            'numeric_fields':{
                 'VOLTAGE 1 ':{'unit': 'V'},
                 'CURRENT 1':{'unit': 'A'},
                 'VOLTAGE 2':{'unit': 'V'},
                 'CURRENT 2':{'unit': 'A'}
             },
             'option_fields':{
                 'POWER SUPPLY':{
                     'options':['1', '2']
                 }
             }


        },
        'CUP01':{
            'numeric_fields':{
                 'VOLTAGE 1 ':{'unit': 'V'},
                 'CURRENT 1':{'unit': 'A'},
                 'VOLTAGE 2':{'unit': 'V'},
                 'CURRENT 2':{'unit': 'A'}
             },
             'option_fields':{
                 'POWER SUPPLY':{
                     'options':['1', '2']
                 }
             }


        }

    },
    'AIR INTAKE':{
        'AIR INTAKE':{
              'option_fields':{
                  'Leakage And Cleaning':{
                      'options':['OK'  , 'NOT OK'],
                      'normal' : 'OK'
                  },
                  'Lighting':{
                      'options':['OK'  , 'NOT OK'],
                      'normal' : 'OK'
                  },
                  'Sound':{
                      'options':['OK'  , 'NOT OK'],
                      'normal' : 'OK'
                  }
                 
             }

        }
    },
     'Fuse box':{
         'Fuse box':{
             'option_fields':{
                 'Fuse BOX no.1':{
                      'options': ['Open', 'Close'], 
                      'normal': 'Open'
                 },
                 'Fuse BOX no.2':{
                      'options': ['Open', 'Close'], 
                      'normal': 'Open'
                     
                 }
             },
             'numeric_fields':{
                 'Voltage 1':{'unit':'V' , 'range':(215,245)},
                 'Current 1':{'unit':'A' , 'range':(None,50)},
                 'Voltage 2':{'unit':'V' , 'range':(215,245)},
                 'Current 2':{'unit':'A' , 'range':(None,50)}
                 
             },

         }
     },
     'BFE&BME':{
         'BFE&BME LV BUS BAR':{
             'option_fields':{
                 'BFE INCOMING BREAKER':{
                      'options': ['Open', 'Close'], 
                      'normal': 'Open'
                 },
                 'BME Incoming  Breaker':{
                      'options': ['Open', 'Close'], 
                      'normal': 'Open'
                 },
                 '220 V DC   AVAILABLE':{
                      'options': ['Yes', 'No'], 
                      'normal': 'Yes'
                 },
                 'Local/Remote Selector':{
                      'options': ['Local', 'Remote'], 
                      'normal': 'Remote'
                 }
             },
             'numeric_fields':{
                 'BFE Bus Bar Voltage':{'unit':'V' , 'range':(390,420)},
                 'BFE Incoming Voltage':{'unit':'V' , 'range':(390,420)},
                 'BFE Incoming Current':{'unit':'A' , 'range':(None,500)},
                 'BME Bus Bar Voltage':{'unit':'V' , 'range':(390,420)},
                 'BME Incoming  Voltage':{'unit':'V' , 'range':(390,420)},
                 'BME Incoming  Current':{'unit':'V' , 'range':(None,250)},
                 'BFE/BME Bus tie Current':{'unit':'A' , 'range':(None,250)},
                 'BLS voltage':{'unit':'V' , 'range':(390,420)},
                 'BLS Current':{'unit':'A'},
                 'BLE voltage':{'unit':'V' , 'range':(390,420)},
                 'BLE Current':{'unit':'A'}
             }
         }
     },
    'DC UPS':{
        'BTL01 BATTERY CHARGER 400VAC/240 VDC':{
            'numeric_fields':{
                'AC input voltage':{'unit' :'V', 'range':(390, 420)},
                'AC input current':{'unit' :'A', 'range':(None, 10)},
                'Load voltage':{'unit' :'V', 'range':(215, 245)},
                'Load current':{'unit' :'A', 'range':(5,30)},
                'Battery voltage':{'unit' :'V', 'range':(215, 245)},
                'Battery current':{'unit' :'A', 'range':(5, 32)}
            },
            'option_fields':{
                'Charger Status':{
                      'options': ['Initial', 'Boost', 'Float'], 
                      'normal': 'Float'
                 },
                'Distribution Of Alarm':{
                      'options': ['Yes', 'No'], 
                      'normal': 'No'
                 }
            }
        },
        'BTL02 BATTERY CHARGER 400VAC/240 VDC':{
            'numeric_fields':{
                'AC input voltage':{'unit' :'V', 'range':(390, 420)},
                'AC input current':{'unit' :'A', 'range':(None, 10)},
                'Load voltage':{'unit' :'V', 'range':(215, 245)},
                'Load current':{'unit' :'A', 'range':(5,30)},
                'Battery voltage':{'unit' :'V', 'range':(215, 245)},
                'Battery current':{'unit' :'A', 'range':(5, 32)}
            },
            'option_fields':{
                'Charger Status':{
                      'options': ['Initial', 'Boost', 'Float'], 
                      'normal': 'Float'
                 },
                'Distribution Of Alarm':{
                      'options': ['Yes', 'No'], 
                      'normal': 'No'
                 }
            }
        },
        'Inverter':{
            'numeric_fields':{
                'Input DC voltage 1':{'unit' :'V', 'range':(210, 245)},
                'Input DC Current 1':{'unit' :'A', 'range':(None, 95)},
                'Out put Voltage 1':{'unit' :'V', 'range':(210, 245)},
                'Output Current 1':{'unit' :'A'},
                'Out put Frequency 1':{'unit' :'Hz', 'range':(49, 51)},
                'Input DC voltage 2':{'unit' :'V', 'range':(210, 245)},
                'Input DC Current 2':{'unit' :'A', 'range':(None, 95)},
                'Out put Voltage 2':{'unit' :'V', 'range':(210, 245)},
                'Output Current 2':{'unit' :'A'},
                'Out put Frequency 2':{'unit' :'Hz', 'range':(49, 51)}
            },
            'option_fields':{
                'Fault and Alarm 1':{
                      'options':['OK'  , 'NOT OK'],
                      'normal' : 'OK'},
                'Fault and Alarm 2':{
                      'options':['OK'  , 'NOT OK'],
                      'normal' : 'OK'}

            }
        },
        'BRA':{
            'numeric_fields':{
                'BRA Voltage':{'unit' :'V'}
            },
            'option_fields':{
                'BRA Incomming':{
                      'options': ['Open', 'Close'], 
                      'normal': 'Close'
                 },
                 'Fault and Alarm':{
                     'options':['OK'  , 'NOT OK'],
                     'normal' : 'OK'
                     
                 }
            }

        },
        'BUB--BUC DISTRIBUTION PANELS':{
                 'numeric_fields':{
                     'BUB BUS BAR  VOLTAGE':{'unit' :'V', 'range':(210, 245)},
                     'BUC BUS BAR  VOLTAGE':{'unit' :'V', 'range':(210, 245)}
                 },
                'option_fields':{
                    'BUB  Incoming  from BTL01':{
                      'options': ['Open', 'Close'], 
                      'normal': 'Open'
                 },
                    'BUS  TIE ':{
                      'options': ['Open', 'Close'], 
                      'normal': 'Open'
                 },
                    'Incoming from BTL 02':{
                      'options': ['Open', 'Close'], 
                      'normal': 'Open'
                 }
                } 
        }
    },
    'CUN':{
        'CUN':{
            'numeric_fields':{
                'Output Voltage     CH1':{'unit' :'V', 'range':(24, None)},
                'Output Current     CH1':{'unit' :'A', 'range' : (None, 25)},
                'Output Voltage     CH2':{'unit' :'V', 'range':(24, None)},
                'Output Current     CH2':{'unit' :'A', 'range' : (None, 25)}
            }
        },
        'LCC Status':{
              'option_fields':{
                  'Lighting ':{
                     'options':['OK'  , 'NOT OK'],
                     'normal' : 'OK'
                     
                 },
                  'HVAC in Service':{
                     'options':['OK'  , 'NOT OK'],
                     'normal' : 'OK'
                     
                 },
                  'Cleaning':{
                     'options':['OK'  , 'NOT OK'],
                     'normal' : 'OK'
                     
                 }
              }  
        }
    },
    'Transformers':{
        'Main Transformer':{
            'option_fields':{
               ' Tap Changer Mode (Local/Remote)':{
                   'options': ['Local', 'Remote'], 
                   'normal': 'Remote'
               },
               'Fans Controller (Auto/manual)':{
                   'options': ['Auto', 'Manual'], 
                   'normal': 'Auto'
               },
               'Transformer oil level':{
                   'options': ['OK', 'NOK'],
                    'normal': 'OK'
               },
               'Tap changer oil level':{
                   'options': ['OK', 'NOK'],
                    'normal': 'OK'
               },
               'Sound&Leakage':{
                   'options': ['OK', 'NOK'],
                    'normal': 'OK'
               }
            },
            'numeric_fields':{
                 'Main trans.  winding temp. HV side':{'unit' :'°C', 'range':(None, 100)},
                 'Main trans.  winding temp. LV side':{'unit' :'°C', 'range':(None, 100)},
                 'Main trans. Oil temp.':{'unit' :'°C', 'range':(None, 80)},
                 'Tap changer position':{'unit': ''}
             }

        },
        'Unit trans':{
            'option_fields':{
                    'Transformer oil level':{
                          'options': ['OK', 'NOK'],
                          'normal': 'OK'
                    },
                    'Sound&Leakage':{
                        'options': ['OK', 'NOK'],
                        'normal': 'OK'
                    }
            },
            'numeric_fields':{
                 'Unit trans.  winding temp.':{'unit' :'°C', 'range':(None, 80)},
                 'Unit trans. Oil temp.':{'unit' :'°C', 'range':(None, 80)}
             }


        }

    },
    'BBE BUS BAR':{
        'BBE BUS BAR':{
             'option_fields':{
                 'All Local/Remote Selector':{
                     'options': ['Local', 'Remote'], 
                     'normal': 'Remote'
                 },
                 'Interconnection to common':{
                     'options': ['Open', 'Close'], 
                    'normal': 'Open'
                 },
                 'Lamp Test of All Feeders':{
                     'options': ['OK', 'NOK'],
                     'normal': 'OK'
                 }
                 
             },
             'numeric_fields':{
                 'Incoming from unit trans. Voltage':{'unit' :'KV'},
                 'Incoming from unit trans .Current':{'unit' :'KA'},
                 'BBE BUS Voltage':{'unit' :'KV'},
                 'BFT Winding Temp A':{'unit' :'°C'},
                 'BFT Winding Temp B':{'unit' :'°C'},
                 'BFT Winding Temp C':{'unit' :'°C'},
                 'BFT Core TEMP':{'unit' :'°C'},
                 'MKC Winding Temp A':{'unit' :'°C'},
                 'MKC Winding Temp B':{'unit' :'°C'},
                 'MKC Winding Temp C':{'unit' :'°C'},
                 'MKC Core TEMP':{'unit' :'°C'}
                 
             }
        }
    },
    'Turbocompressor':{
        'Turbocompressor':{
            'option_fields':{
                'Flames':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'
                },
                'Combustion Chamber ':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'
                },
                'Comp. Air Dryer':{
                    'options':['ON', 'OFF'],
                },
                'Leakage And Sound.':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'
                }
            },
            'numeric_fields':{
                'Turbine Cooling Air':{'unit' :'BAR', 'range':(0.1, 0.2)}
            }
        }
    },
    'Battery Room':{
        'Battery Room':{
            'numeric_fields':{
                'Temp.':{'unit':'ºc', 'range':(20, 25)}
            },
            'option_fields':{
                'Ventilation fan number  in service':{
                    'options':['1', '2']
                },
                'Level of Battery':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'

                },
                'Battery Sulphated':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'

                },
                'Clraning':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'

                },
                'Lighting ':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'

                }
            }
        }
    },
    'HYDR.SKID':{
        'HYDR.SKID':{
            'numeric_fields':{
                'Hyd. Pump 1 Press.':{'unit' :'bar', 'range':(155, 165)},
                'Hyd. Pump 2 Press.':{'unit' :'bar', 'range':(155, 165)},
                'Hyd. Oil Press.':{'unit' :'bar', 'range':(155, 165)},
                'Accumolator 1 Press.':{'unit' :'bar', 'range':(155, 165)},
                'Accumolator 2 Press.':{'unit' :'bar', 'range':(155, 165)},
                'Hyd. Oil Temp.':{'unit' :'ºc', 'range':(35, 60)},
                'Hyd. Oil  Cooling Loop Press.':{'unit' :'bar', 'range':(2.5 , 3.5)},

            },
            'option_fields':{
                'Hyd. Tank Level':{
                    'options':['Low', 'Normal' , 'High'] ,
                    'normal' : 'Normal'
                },
                'Sound Of Motors':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'
                },
                'Leakage And Cleaning':{
                    'options': ['OK', 'NOK'],
                    'normal': 'OK'
                }
            }

        }
    },
    'Diesel Pump Container':{
        'Diesel Pump PUMP NO.1':{
            'numeric_fields':{
                'Level of fuel (%)':{'unit' :'', 'range':()},
                'Voltage of Battery no.1':{'unit' :'', 'range':()},
                'Voltage of Battery no.2':{'unit' :'', 'range':()},
                'Pressure of line':{'unit' :'', 'range':()}
            },
            'option_fields':{
                'Level of Coolant(water)':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'},
                'Level of oil':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'},
                'HEATER':{
                    'options':['on', 'off']
                },
                'Outlet valve':{
                    'options':['Open', 'Close']
                },
                'Auto/Man/Off':{
                    'options':['Auto','Man', 'Off' ]
                },
                'Alarm and fault':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'}
            }
        },
        'Diesel Pump PUMP NO.2':{
            'numeric_fields':{
                'Level of fuel (%)':{'unit' :'', 'range':()},
                'Voltage of Battery no.1':{'unit' :'', 'range':()},
                'Voltage of Battery no.2':{'unit' :'', 'range':()},
                'Pressure of line':{'unit' :'', 'range':()}
            },
            'option_fields':{
                'Level of Coolant(water)':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'},
                'Level of oil':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'},
                'HEATER':{
                    'options':['on', 'off']
                },
                'Outlet valve':{
                    'options':['Open', 'Close']
                },
                'Auto/Man/Off':{
                    'options':['Auto','Man', 'Off' ]
                },
                'Alarm and fault':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'}
            }
        },
        'GENERAL CHECK':{
            'numeric_fields':{
                'Level of  Water':{'unit' :'', 'range':()}
            },
            'option_fields':{
                'Fire Panel ':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'},
                'Lighting ':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'},
                'Ventilation':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'},
                'Cleaness':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'}
            }
        }
    },
    'MV BUS BCA BCB':{
        'MV BUS BCA/BCB':{
             'numeric_fields':{
                 'BCA BUS BAR Voltage':{'unit' :'kv', 'range':(6.4 , 6.8)},
                 'BCB BUS BAR Voltage':{'unit' :'kv', 'range':(6.4 , 6.8)},
                 'Current of Incoming 1':{'unit' :'A(sepam)'},
                 'Voltage of Incoming 1':{'unit' :'V(sepam)', 'range':(6.4 , 6.8)},

             },
             'option_fields':{
                 'BUS TIE':{
                     'options': ['Open', 'Close'], 
                     'normal': 'Open'
                 },
                 'Bus Tie Lock Out Relay':{
                     'options':['Set', 'Reset'],
                     'normal': 'Reset'
                 },
                 'INCOMING FROM UNIT 1':{
                     'options': ['Open', 'Close'], 
                     'normal': 'Close'
                 },
                 'Incoming 1 Lock Out Relay':{
                     'options':['Set', 'Reset'],
                     'normal': 'Reset'
                 },
                 'Incoming 1 Earth Switch':{
                     'options': ['Open', 'Close'], 
                     'normal': 'Open'
                 },
                 'INCOMING FROM UNIT 2':{
                     'options': ['Open', 'Close'], 
                     'normal': 'Close'
                 },
                 'REMOTE POS FOR BUS TIE':{
                     'options': ['Local', 'Remote'], 
                     'normal': 'Remote'
                 },
                 ' Lamp Test OF All Feeders':{
                     'options': ['OK', 'NOK'],
                     'normal': 'OK'
                 }
             }
             
        }
    },
    'LV BUS':{
        'LV BUS BHA/BHB':{
            'numeric_fields':{
                'BHA Incoming Voltage1':{'unit' :'V', 'range':(380, 420)},
                'BHA Bus Voltage1':{'unit' :'V', 'range':(380,420)},
                'BHA Incoming Current1':{'unit' :'A'},
                'BHB Incoming Voltage2':{'unit' :'V', 'range':(380,420)},
                'BHB Bus Voltage2':{'unit' :'V', 'range':(380,420)},
                'BHB Incoming Current2':{'unit' :'A'}
            },
            'option_fields':{
                'Incoming  From BHT01':{
                    'options': ['Open', 'Close'], 
                     'normal': 'Close'
                },
                'Incoming 1 TCS & Lock Out':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'
                },
                'BHA Incoming DC Healthy':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'
                },
                'BUS TIE':{
                     'options': ['Open', 'Close'], 
                     'normal': 'Open'
                },
                'LOCAL/REMOTE Selector':{
                    'options': ['Local', 'Remote'], 
                     'normal': 'Remote'
                },
                'Incom. From BHT02':{
                    'options': ['Open', 'Close'], 
                     'normal': 'Close'
                },
                'Incoming 2 TCS & Lock Out':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'
                }
            }
        }
    },
    'LV EMERGANCY BUS BAR':{
        'BMC BUS BAR':{
            'numeric_fields':{
                'Incoming 1 Voltage(BHA)':{'unit' :'V', 'range':(380, 420)},
                'Incoming 2 Voltage(BMA)':{'unit' :'V', 'range':(380, 420)}
            },
            'option_fields':{
                'Energized From INCOMING 1/2':{
                    'options':['1', '2']
                },
                'AUTO/MANUAL Selector':{
                    'options': ['Auto', 'Manual'], 
                    'normal': 'Auto'
                }
            }
        },
        'LV EMERGENCY BUS BAR BMA / BMB':{
            'numeric_fields':{
                'BMA incoming voltage':{'unit' :'V', 'range':(380, 420)},
                'BMA bus voltage':{'unit' :'V', 'range':(380, 421)},
                'BMA incoming current':{'unit' :'A'},
                'BMB incoming voltage':{'unit' :'V', 'range':(380, 420)},
                'BMB BUS voltage':{'unit' :'V', 'range':(380, 421)},
                'BMB incoming current':{'unit' :'A'},

            },
            'option_fields':{
                'incoming from BHA':{
                    'options': ['Open', 'Close'], 
                    'normal': 'Close'
                },
                'Incom. From BHB':{
                    'options': ['Open', 'Close'], 
                    'normal': 'Close'
                },
                'LOCAL/REMOTE Selector':{
                    'options': ['Local', 'Remote'], 
                    'normal': 'Remote'
                },
                'Fault and alarm':{
                    'options': ['OK', 'NOK'],

                }
            }
        }
    },
    'FIN FAN SKID':{
        'FIN FAN SKID':{
            'numeric_fields':{
                'Pump In Service Suction Press':{'unit' :'bar', 'range':(0.25, None)},
                'Pump In Service Disch. Press':{'unit' :'bar', 'range':(3, None)},
                'Tube Bundle 1 Outlet Temp.':{'unit' :'ºc', 'range':(8, 48)},
                'Tube Bundle 2 Outlet Temp.':{'unit' :'ºc', 'range':(8, 48)},
                'Water Inlet Cooler Temp.':{'unit' :'ºc', 'range':(10 , 60)},
                'CCW Pump Disch. Temp':{'unit' :'ºc', 'range':(8, 48)},
                'Pump In Service Strainer  DP':{'unit' :'bar', 'range':(None, 0.35)},

            },
            'option_fields':{
                'Pump In Service':{
                    'options':['1', '2']
                }
,
                'Surge Tank Level':{
                    
                     'options': ['OK', 'NOK'],
                     'normal': 'OK'
                },
                ' Pump Oil Level':{
                    
                     'options': ['OK', 'NOK'],
                     'normal': 'OK'
                }
            }
        }
    },
    'OUTDOOR&INDOOR GAS SKID':{
        'OUTDOOR & INDOOR GAS SKID':{
            'numeric_fields':{
                'Fuel Gas Duplex Filter In Service ΔP' :{'unit' :'bar', 'range':(None, 0.35)},
                'Fuel Gas Duplex Filter In Service Press. ' :{'unit' :'bar', 'range':(19 , 22)},
                'Final Chance Filter Pressure' :{'unit' :'bar', 'range':(18, 22)},
                'Final Chance filter DP' :{'unit' :'bar', 'range':(None, 0.35)},
                'Pressure Before Strainer' :{'unit' :'bar', 'range':(18, 22)}
            },
            'option_fields':{
                'Fuel Gas Duplex Filter In Service':{
                    'options':['1', '2']
                },
                'Fuel Gas Duplex Filter Level':{
                    'options':['normal', 'unnormal'],
                    'normal' : 'normal'
                },
                'Line In Service':{
                    'options':['Main', 'Bypass'],
                    'normal' : 'Main'
                },
                'Final Chance Filter Level':{
                    'options':['normal', 'unnormal'],
                    'normal' : 'normal'
                },
                'Enclosure Fan In Service':{
                    'options':['1', '2']
                },
                'Lighting and Leakage':{
                    
                     'options': ['OK', 'NOK'],
                     'normal': 'OK'
                }
            }
        }
    },
    'BHT TRANS':{
            'BHT01':{
                'numeric_fields':{
                    'Oil Temp' :{'unit' :'**'},
                    'Conservator Level' :{'unit' :'%'}

                },
                'option_fields':{
                    'Leakage & Sound':{
                        'options': ['OK', 'NOK'],
                        'normal': 'OK'
                    }
                }
            },
            'BHT02':{
                'numeric_fields':{
                    'Oil Temp' :{'unit' :'**'},
                    'Conservator Level' :{'unit' :'%'}

                },
                'option_fields':{
                    'Leakage & Sound':{
                        'options': ['OK', 'NOK'],
                        'normal': 'OK'
                    }
                }
            }
        
    },
    "Inverter 220vdc 220vac":{
        'Inverter no.1':{
            'numeric_fields':{
                'Dc input Voltage':{'unit' :'V', 'range':(210, 245)},
                'Dc input Current':{'unit' :'A', 'range':(None, 95)},
                'Inverter Voltage ':{'unit' :'V', 'range':(210, 245)},
                'Inverter Current ':{'unit' :'A'},
                'Inverter Frequency':{'unit' :'Hz', 'range':(49 , 51)}

            }, 
            'option_fields':{
                'Lamp test':{
                        'options': ['OK', 'NOK'],
                        'normal': 'OK'
                    },
                'Fault and alarm':{
                        'options': ['OK', 'NOK'],
                        'normal': 'OK'
                    }
            }
        },
        'Inverter no.2':{
            'numeric_fields':{
                'Dc input Voltage':{'unit' :'V', 'range':(210, 245)},
                'Dc input Current':{'unit' :'A', 'range':(None, 95)},
                'Inverter Voltage ':{'unit' :'V', 'range':(210, 245)},
                'Inverter Current ':{'unit' :'A'},
                'Inverter Frequency':{'unit' :'Hz', 'range':(49 , 51)}

            }, 
            'option_fields':{
                'Lamp test':{
                        'options': ['OK', 'NOK'],
                        'normal': 'OK'
                    },
                'Fault and alarm':{
                        'options': ['OK', 'NOK'],
                        'normal': 'OK'
                    }
            }
        },
        'BRA/B 220 V ac':{
            'numeric_fields':{
                'BRA Voltage':{'unit' :'V', 'range':(210, 250)},
                'BRA Current':{'unit' :'A', 'range':()},
                'BRB Voltage':{'unit' :'V', 'range':()},
                'BRB Current':{'unit' :'A', 'range':(210, 250)},
                'By Pass Voltage':{'unit' :'V', 'range':(210 , 250)}
            },
            'option_fields':{
                'static switch 1/2 by pass':{
                    'options':['1', '2'],
                    'normal': '1'
                },
                'fault and alarm':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'
                }
            }
        }
    },
    'Electical Fire container':{
        'MV PUMP 1':{
            'numeric_fields':{
                'LINE PRESS':{'unit' :'', 'range':()}
            },
            'option_fields':{
                'OUTLET VLV':{
                    'options': ['Open', 'Close']
                },
                'PANEL':{
                    'options': ['OK', 'NOK']
                },
                'COMMANDER':{
                    'options': ['Auto', 'Manual']
                }
            }
        },
        'MV PUMP 2':{
            'numeric_fields':{
                'LINE PRESS':{'unit' :'', 'range':()}
            },
            'option_fields':{
                'OUTLET VLV':{
                    'options': ['Open', 'Close']
                },
                'PANEL':{
                    'options': ['OK', 'NOK']
                },
                'COMMANDER':{
                    'options': ['Auto', 'Manual']
                }
            }
        },
        'JUCKEY PUMP 1':{
            'numeric_fields':{
                'LINE PRESS':{'unit' :'', 'range':()}
            },
            'option_fields':{
                'OUTLET VLV':{
                    'options': ['Open', 'Close']
                },
                'PANEL':{
                    'options': ['OK', 'NOK']
                },
                'COMMANDER':{
                    'options': ['Auto', 'Manual']
                }
            }
        },
        'JUCKEY PUMP 2':{
            'numeric_fields':{
                'LINE PRESS':{'unit' :'', 'range':()}
            },
            'option_fields':{
                'OUTLET VLV':{
                    'options': ['Open', 'Close']
                },
                'PANEL':{
                    'options': ['OK', 'NOK']
                },
                'COMMANDER':{
                    'options': ['Auto', 'Manual']
                }
            }
        },
        'Accumulator':{
             'numeric_fields':{
                 'PRESS':{'unit' :'', 'range':()}
             },
             'option_fields':{
                 'MAIN VLV':{
                     'options': ['Open', 'Close']
                 },
                 'DRAIN VLV':{
                    'options': ['Open', 'Close']
                 }
             }
        },
        'CONTAINER':{
            'option_fields':{
                'LIGHT. & VENT. PANEL':{
                    'options': ['OK', 'NOK']
                },
                'FIRE PANEL':{
                    'options': ['OK', 'NOK']
                },
                'LEAKAGE':{
                    'options': ['OK', 'NOK']
                },
                'FAULT & ALARM':{
                    'options': ['OK', 'NOK']
                },
                'CLEANLINESS':{
                    'options': ['OK', 'NOK']
                },
                'RESERVOIR LVL':{
                    'options': ['OK', 'NOK']
                }
            }
        }
    },
    'BUB BUC':{
        'BTL01':{
            'numeric_fields':{
                'AC Input Voltage':{'unit' :'V', 'range':(380, 420)},
                'AC Input Current':{'unit' :'A'},
                'Input Frequency':{'unit' :'Hz', 'range':(49,51)},
                'Charge Voltage':{'unit' :'V', 'range':(210, 245)},
                'Charge Current':{'unit' :'A'},
                'Load Voltage':{'unit' :'V'}
            },
            'option_fields':{
                'Charger Status':{
                    'options': ['Initial', 'Boost', 'Float'], 
                    'normal': 'Float'
                },
                'Fault and alarm':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'
                },
                'Lamp test':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'
                }
            }
        },
        'BTL02':{
            'numeric_fields':{
                'AC Input Voltage':{'unit' :'V', 'range':(380, 420)},
                'AC Input Current':{'unit' :'A'},
                'Input Frequency':{'unit' :'Hz', 'range':(49,51)},
                'Rec. Voltage':{'unit' :'V', 'range':(210, 245)},
                'Rec. Current':{'unit' :'A'},
                'Load Voltage':{'unit' :'V'}
            },
            'option_fields':{
                'Charger Status':{
                    'options': ['Initial', 'Boost', 'Float'], 
                    'normal': 'Float'
                },
                'Fault and alarm':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'
                },
                'Lamp test':{
                    'options': ['OK', 'NOK'],
                     'normal': 'OK'
                }
            }
        },
        'BUB':{
            'numeric_fields':{
                'BUB load Voltage':{'unit' :'V'},
                'BUB load Current':{'unit' :'A'}
            }
        },
        'BUC':{
            'numeric_fields':{
                'BUB load Voltage':{'unit' :'V'},
                'BUB load Current':{'unit' :'A'}
            }
        }
        
    },
    'Gen.coolers':{
        'Gen. coolers':{
            'numeric_fields':{
                'Actual Load':{'unit' :'MW', 'range':(0, 180)},
                'Gen. cooler 1 outlet temp':{'unit' :'ºc', 'range':(10 , 45)},
                'Gen. cooler 2 outlet temp':{'unit' :'ºc', 'range':(10 , 45)},
                'Gen. cooler 3 outlet temp':{'unit' :'ºc', 'range':(10 , 45)},
                'Gen. cooler 4 outlet temp':{'unit' :'ºc', 'range':(10 , 45)},
                'Gen cooler 1  DP':{'unit' :'mbar', 'range':(None, 2000)},
                'Gen cooler 2  DP':{'unit' :'mbar', 'range':(None, 2000)},
                'Gen cooler 3  DP':{'unit' :'mbar', 'range':(None, 2000)},
                'Gen cooler 4  DP':{'unit' :'mbar', 'range':(None, 2000)},
                'GEN  lube oil CE Return Press':{'unit' :'bar', 'range':(1.8 , None)},
                'GEN  lube oil OCE Return Press':{'unit' :'bar', 'range':(1.8 , None)}
            },
            'option_fields':{
                'UNIT IN: OPER/TURN/STANDSTILL':{
                    'options': ['OP' , 'TG' , 'SS']
                }
            }
        }
    }


}

# :{'unit' :'', 'range':()}
# :{
#                     'options':['1', '2']
#                 }

# 'options': ['Auto', 'Manual'], 
#                     'normal': 'Auto'

# 'options': ['Open', 'Close'], 
#                     'normal': 'Open'


# 'options': ['Local', 'Remote'], 
#                      'normal': 'Remote'

# 'options': ['OK', 'NOK'],
#                      'normal': 'OK'