#DESENVOLVIDOR BY:LEANDROTN CRIPTROGRAFRADO POR MOTIVO DE SEGURANÇA
import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzICNsaW5lOjE6aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgdGltZSAjbGluZToyOmltcG9ydCB0aW1lDQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlICxpbml0ICNsaW5lOjM6ZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgaW5pdA0KcHJpbnQgKGYiIiJ7Rm9yZS5HUkVFTn0NCiAvJCQkJCQkJCAvJCQgICAgICAgICAgICAgICAgICAgICAgICAvJCQkJCQkJCQgICAgICAvJCQNCnwgJCRfXyAgJHxfXy8gICAgICAgICAgICAgICAgICAgICAgIHxfXyAgJCRfXy8gICAgIHwgJCQNCnwgJCQgIFwgJCQvJCQgLyQkJCQkJCQgLyQkJCQkJCQgLyQkJCQkJHwgJCQgLyQkJCQkJHwgJCQgICAvJCQgLyQkJCQkJCAvJCQkJCQkJA0KfCAkJCAgfCAkfCAkJC8kJF9fX19fLy8kJF9fX19fLy8kJF9fICAkfCAkJC8kJF9fICAkfCAkJCAgLyQkLy8kJF9fICAkfCAkJF9fICAkJA0KfCAkJCAgfCAkfCAkfCAgJCQkJCQkfCAkJCAgICAgfCAkJCAgXCAkfCAkfCAkJCAgXCAkfCAkJCQkJCQvfCAkJCQkJCQkfCAkJCAgXCAkJA0KfCAkJCAgfCAkfCAkJFxfX19fICAkfCAkJCAgICAgfCAkJCAgfCAkfCAkfCAkJCAgfCAkfCAkJF8gICQkfCAkJF9fX19ffCAkJCAgfCAkJA0KfCAkJCQkJCQkfCAkJC8kJC'
love = 'DxWPDxsPNtWPDxWPDxsPNtWPDxWPDxsPNxsPNtWPDxWPDxsPNxWPOpVPNxsPNtWPDxWPDxsPNxWPNtsPNxWN0XsS9sK19sK18isS9ssS9sK19sK18iVSksK19sK19sY1ksK19sK18isS9sY1ksK19sK18isS9sYlNtKS9sY1ksK19sK19ssS9sYlNtsS9sYj0XQDbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVN0Xr0MipzHhHxIRsILtZP4jYwS7Ez9lMF5UHxISGa0APyfgKFOREIASGyMCGSMWER8tr0MipzHhHxIRsGbmr0MipzHhE1WSEH59VTW5VCPqxVijaMPR8W2DtCPqxV3jaMPQ8W2DxsPqxV7jaMPG8W2DwFZ3AwL5QDbAPyijaMPY8W2DuCPqxVQjaMPA8W2Dt/PqxWUjaMPB8W2Dx/PqxV0wAmL2BI0tHT9lVRMuqz9lVT7Qb28tqJk0pzSjLKAmMFOiVTkcoJy0MFOxMFN1ZPO0o2gyoaZtpT9lVUMyrt0XVvVvXFAfnJ5yBwVmBvxAPaEeoz5uoJHtCJyhpUI0VPtvHIIOGPOCVR5CGHHtERRtH1IOVRkWH1EOVRESVSECF0IBBvNvXFAfnJ5yBwV0BaEeoz5uoJHtCFOcoaO1qPtvHIIOGPOCVR5CGHHtERRtH1IOVRkWH1EOVRESVSECF0IBBvNvXD0Xq2y0nPOipTIhVPuzVag0n25hLJ1ysFVfVaVvXJSmVTLtBvAfnJ5y'
god = 'OjI1OndpdGggb3BlbihmInt0a25uYW1lfSIsICJyIikgYXMgZjoNCiAgICBmb3IgbGluZSBpbiBmIDojbGluZToyNjpmb3IgbGluZSBpbiBmOg0KICAgICAgICB0aW1lIC5zbGVlcCAoMSApI2xpbmU6Mjc6dGltZS5zbGVlcCgxKQ0KICAgICAgICB0b2tlbiA9bGluZSAucnN0cmlwICgiXG4iKSNsaW5lOjI4OnRva2VuID0gbGluZS5yc3RyaXAoIlxuIikNCiAgICAgICAgaGVhZGVycyA9eyJBdXRob3JpemF0aW9uIjpmInt0b2tlbn0ifSNsaW5lOjI5OmhlYWRlcnMgPSB7IkF1dGhvcml6YXRpb24iOiBmInt0b2tlbn0ifQ0KICAgICAgICBzcmMgPXJlcXVlc3RzIC5nZXQgKCJodHRwczovL2Rpc2NvcmRhcHAuY29tL2FwaS92Ni9hdXRoL2xvZ2luIixoZWFkZXJzID1oZWFkZXJzICkjbGluZTozMDpzcmMgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8vZGlzY29yZGFwcC5jb20vYXBpL3Y2L2F1dGgvbG9naW4iLCBoZWFkZXJzPWhlYWRlcnMpDQogICAgICAgIHRyeSA6I2xpbmU6MzI6dHJ5Og0KICAgICAgICAgICAgaWYgc3JjIC5zdGF0dXNfY29kZSA9PTIwMCA6I2xpbmU6MzM6aWYgc3JjLnN0YXR1c19jb2RlID09IDIwMDoNCiAgICAgICAgICAgICAgICBwcmludCAoZiJ7Rm9yZS5HUkVFTn1bLV0ge0Zvcm'
destiny = 'HhHxIGEIE9IT9eMJ4tMaIhL2yiozRuVQ4tVvg0o2gyovNcV2kcozH6ZmD6pUWcoaDbMvW7Ez9lMF5UHxISGa1oYI0tr0MipzHhHxIGEIE9IT9eMJ4tMaIhL2yiozRuVQ4tVvNeVUEin2IhXD0XVPNtVPNtVPNtVPNtMJkmMFN6V2kcozH6ZmH6MJkmMGbAPvNtVPNtVPNtVPNtVPNtVPOjpzyhqPNbMvW7Ez9lMF5FEHE9Jl1qVUgTo3WyYyWSH0IHsIEin2IhVTyhqfBuoTyxol4tCvNvX3Ein2IhVPxwoTyhMGbmAwcjpzyhqPuzVagTo3WyYyWSEU1oYI0tr0MipzHhHxIGEIE9IT9eMJ4tnJ52j6SfnJEiYvN+VPVtXlO0o2gyovxAPvNtVPNtVPNtMKuwMKO0VRI4L2IjqTyiovN6V2kcozH6Zmp6MKuwMKO0VRI4L2IjqTyiowbAPvNtVPNtVPNtVPNtVUOlnJ50VPtvDJkaolOkqJIvpz91VT8tL29hqTS0olOwo20tolOmqKOipaEyVTEcp2AipzDto3HtLJAioaEyj6qyqFOuoTq1oFOjpz9voTIgLFN6XFVcV2kcozH6Zmt6pUWcoaDbVxSfM28tpKIyLaWiqFOiVTAioaEuqT8tL29gVT8tp3Ijo3W0MFOxnKAwo3WxVT91VTSwo250MpBaMKHtLJkaqJ0tpUWiLzkyoJRtBvxvXD0XpUWcoaDtXPWJMKWcMzywLpBaj6AiVTAiozAfqpBgMTRuVvxwoTyhMGbmBGcjpzyhqPtvIzIlnJMcL2UQc8BwolOwo25woUKQeJEuVFVcQDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))