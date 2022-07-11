# simulo un .env con python ya que en este caso no tiene sentido utilizar un .env

class Settings:
    urlForFindLocation = 'https://www.google.com/search?'
    urlForFindRestos = 'https://www.google.com/search?tbs=lf:1,lf_ui:9&tbm=lcl&'

    urlApiGeo='https://api.opencagedata.com/geocode/v1/json?q=40.439262+-3.7732129&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en'


    params = {
        'sxsrf': 'ACYBGNQ16aJKOqQVdyEW9OtCv8zRsBcRig:1575650951873',
        'source': 'hp',
        'ei': 'h4bqXcT0MuPzqwG87524BQ',
        'q': '',
        'oq': '',
        'gs_l': 'psy-ab.1.1.35i362i39l10.0.0..139811...4.0..0.0.0.......0......gws-wiz.....10.KwbM7vkMEDs'
    }

    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'private, max-age=0',
            'cookie': 'SEARCH_SAMESITE=CgQIwpUB; SID=KQh4fCKnabgxPSQV-o3Kiagc2dg7xZq7MURVrZ1S6SiAUBBRz4BJHKCUSL9eB2Q9B_Lh4Q.; __Secure-1PSID=KQh4fCKnabgxPSQV-o3Kiagc2dg7xZq7MURVrZ1S6SiAUBBRt1_rx6r49cjSKmVWviP--Q.; __Secure-3PSID=KQh4fCKnabgxPSQV-o3Kiagc2dg7xZq7MURVrZ1S6SiAUBBRyjSWViNRTJFK2LY_m2goMw.; HSID=A2xX3wCSo_7Z0b8VT; SSID=AmnAI4Ljco5IBEIgT; APISID=nnBvlt_m1zKSu1bm/A89jJ-PtI9-DYBQTB; __Secure-1PAPISID=Up4Nc90sYt8HeS4u/AgZi5w5XgilDDA_Q2; SAPISID=Up4Nc90sYt8HeS4u/AgZi5w5XgilDDA_Q2; __Secure-3PAPISID=Up4Nc90sYt8HeS4u/AgZi5w5XgilDDA_Q2; SIDCC=AJi4QfHMmZRfF_C2Yc7beIA046d5cmNs4ycxavO7UHRHXhmmI17_FArEPhHxUK4NUEAidXsaYA; __Secure-3PSIDCC=AJi4QfHp7RwWyFH51T1pEYtkG4DPlpDwnP3e-phOqUGqTPJrYHueU0CRSjbzkNFyZ1kXlz3_jg; AEC=AakniGPYZcbgGFa59AavK-t1EiTDuz79hHNI1HG9dXEqE8MGu9lDAqKYp84; 1P_JAR=2022-07-10-03; SOCS=CAISNQgCEitib3FfaWRlbnRpdHlmcm9udGVuZHVpc2VydmVyXzIwMjIwNzA1LjE2X3AwGgJlcyACGgYIgNCtlgY; NID=511=kd67fPtTqul_--Ujmb3-nTYfIoEuZI4Lbx6ntD1E2lczAJ3FI2CvL-fHcj6Pomfm0fmfkT8Ild-T7QZbrE8yLaXTH2Oy6oAQ97J17q4JS-bi3rOk1dDCL7WMnq0Zfogg_RoQRultpLDwUxL1SI62AnBhMrkWepA4ZxZlChXS9wgTgNbCo_I; DV=wzK0Q_glAlQaMLoqspk1c5EXz8q_Hhg; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjU3NTIxNjE0NDAxMDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDQwNDEzNDA2OAogIGxvbmdpdHVkZV9lNzogLTM3MDY2MDE3Cn0KcmFkaXVzOiA4MTE4LjkwMDAwMDAwMDAwMQpwcm92ZW5hbmNlOiA2Cg==',
            # 'cookie': 'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; HSID=AenmNVZxnoADsXz_x; SSID=AjbLhhwkjh8f3FOM8; APISID=IqkNtUA0V2DXlees/A0tA9iPSadMC2X6dt; SAPISID=8-N4B06I_D5N1mvR/AleccT6Zt0QllrukC; CONSENT=YES+UA.en+; OTZ=5204669_48_48_123900_44_436380; SID=rAd3UAFN_dCIGQ87HqDZZGiNyxdz0dL4dZKy_XquqSr_CHTzqSzfDdNTfLmA2xCMEZOZMA.; ANID=AHWqTUnDWUSHdvWhJiIoPxMAKYXmVtHCQIq7LBMYgiSlZZr3AMGTwY2aVUdjeY7z; NID=193=QImFbOa1vnKpflG8yJytqPXbJYJ9k8fWbIzQMGExsMa4g5oJwdnI56WNjgEVFAyAPJ1SEEOQ-zlW4HAUv-JLj0yAUImTgeT1syDIgFTMWAqxdz10lWRlzFC-3Fmjv6xJcqm2o6RKI50dmb7GetiheNdSAYPkAjng_c0lOHoXZLmtMwFOpkPTrQwVyUW8R2x4o1ux3OW3_kEbR_BREowRV8lVqrsnyo1ffC_Pm40zf81k7aS0cv9esYweGHF6Lxd532z4wA; 1P_JAR=2019-12-06-16; DV=k7BRh0-RaJtZsO9g7sjbrkcKoUjC7RYhxDh5AdfYgQAAAID1UoVsAVkvPgAAAFiry7niUB6qLgAAAGCQehpdCXeKnikKAA; SEARCH_SAMESITE=CgQIvI4B; SIDCC=AN0-TYv-lU3aPGmYLEYXlIiyKMnN1ONMCY6B0h_-owB-csTWTLX4_z2srpvyojjwlrwIi1nLdU4',
            'pragma': 'no-cache',
            'referer': 'https://www.google.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.142 Chrome/75.0.3770.142 Safari/537.36'
        }



def secretkey():
    secretkey='jdaksdjsakldjsakldas'
    return secretkey
