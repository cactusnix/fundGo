import requests

# 积分签到详情接口 token
url1 = "https://act.10010.com/SigninApp/signin/getContinuous"
# 首页信息接口 token use this to get token and acc
url2 = "https://m.client.10010.com/mobileserviceimportant/home/queryUserInfoSeven"
# 获得积分接口 token
url3 = "https://act.10010.com/SigninApp/signin/getIntegral"
# 积分签到接口 token
url4 = "https://act.10010.com/SigninApp/signin/daySign"
# 余量查询接口 token and acc
url5 = "https://m.client.10010.com/mobileservicequery/operationservice/queryOcsPackageFlowLeftContent"
r = requests.post(
    url=url4,
    cookies={
        "ecs_token":
        "eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc1YThhMjBiZmJjYWIwZDNhOTI4NTNkYTcwODBmZGRlYjg4YzZjYTI0ODc2YmYzMTRkOTFhY2YzODMwZDEyNTQyNDYxNTVjN2I3ZmY2YWU2ZTY2NWY5ZTJmZGFlN2FhYTZjMTk4MDAzNzFlZmVhMDVhZmU4YzI2NWI0OTJmYmExZjE2NzViNDE1YmFmYTUzZTEzYWFmNWU1YzZjZDQ2NDQxIiwidmVyc2lvbiI6IjAwIn0=",
        "ecs_acc":
        "imVkRDMlES3Zr5BsEuwP9IkM3krcAOgBEQH+Jpvpj5ObXLpe7nRk/Pgy2UiT1X5rHD8D4CYZboA4Y9QE3vy2c/TeOP5mCudHJ+JoY62G6jpvvfqKD0emyJFX5ghIpYtYyrdTlsDrIQFg7FBF314dc4IrxeMQQaOL0MluUIcL4Y8="
    },
    headers={
        'user-agent':
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;unicom{version:iphone_c@8.0200}{systemVersion:dis}{yw_code:}'
    })
print(r.json())

# appID = "bcbf9239dffadd5449045269ab5346e825b1fefbd30873685ad7e92713f4745f2285e4edea5d528b8d5530a61d944b7dee1c657f7d5e863aadba726efdcc2cc645232164217164f203f9e48d9ac8e30553fdad77b2a8c55d9242033ac4ae60ab"

# a_token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTc3NzkxMTUsInRva2VuIjp7ImxvZ2luVXNlciI6IjEzMTE2NzMwODAxIiwicmFuZG9tU3RyIjoieWhmMzU5OGExNjE3MTc0MzE1In0sImlhdCI6MTYxNzE3NDMxNX0.A57wbhLV62qyl0VX_BhyigF6lpMBt2Vp0PbVaTeDqTm9LzcMl31B-GbannWht1CGynefYX7FCwYsb5dcbXF32g; c_id=4301cbc54d2cbe2d58b24a2ec6a3551e66afa2041994cb5021389f0ce6905b78; enc_acc=jjv5lRCcVL0I+58QjMBaSmwCerkPCsY9MoOBe65L1dEQRi0xAkH1zgaLVy2NUT5C4UBf5RYJaHmqn+ifNXhkIlWmDx997a8HB8LnrNcsYcmbKbHVF7LPNA/GzJzR5u2bngXQDM+u4ykj78hkiT9MdGyz6Pk1MORVstS4p4Bgi6s=; invalid_at=c29e0d1d1cdf5dc8741650a44b9feca5f6441a3719b95f089d893e15b280e307; random_login=0; t3_token=b32ec5db7e5bdf1267578b4c56b784ca; third_token=eyJkYXRhIjoiMTMyYzJlNGFmOTFiOWU0ZTRmMmMyMDQwOWVkNWU5NDJiOGU3NzQ1ZWM2MDQzNmEwY2M0ODc0ODRkYjQ2NWJjZjVkNjY5ZjRlOWI3ZTgwN2QxODQyMWY0MmZkZDVjOGE1Njk0NmVjZmZlMGIwMTc4NjVmNjFjOTU4NjFhMjI2YmE1Zjk2MWNmMzFlNDFlNjYxOTE3ZTE5YmFlMDVhYWU3YSIsInZlcnNpb24iOiIwMCJ9; u_areaCode=360; u_type=11; wo_family=0; c_version=iphone_c@8.0200; channel=GGPD; city=036|360; cw_mutual=7064d003eb3c8934e769e430ecf3d64a91246651671794c1a45e99ee80d5d0db9421693c252fde46ceabfc9e119b26c016ee2c56776f417262d225edaba38f79; devicedId=17B204F6-E3F3-4278-9311-D768200FBC05; ecs_token=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxMzExNjczMDgwMSIsInBybyI6IjAzNiIsImNpdHkiOiIzNjAiLCJpZCI6IjBkY2FhNjJmZDU2M2ZjOTk0NzFlZDBhMzc1MDM0NmUzIn0.TtG50G1nz-2W_CF3FxahlCgbCbksG2kOuFCKunGDwjg; login_type=01; ecs_acc=u+S74KbpUWLpR86snVkw8oqilYkIdI0UFsssVut/AMyvkXp8vE1Nxb3QmurrXSPvnsm8Aomc9P3a9CoCFeTtIotA0LYO0+TmVDjj1HLkVyExupeGO+f8Igb90mZFv58Qd5XVLvZHJ+y80oO3wvqapIl9yTAS0OGBhtOBuvoi2LE=; c_mobile=13116730801; c_sfbm=234g_00; logHostIP=null; mobileService1=Ht-MOJQYKe4mApRV1HIJDbJ0YtyI0mX8jupynyEQOjCbm32R5QPv!-1342336473; mobileServiceAll=df436af5efb40ac19f55fedb195c9040; u_account=13116730801; clientid=98|0; custId=13116730801; mallcity=36|360; tianjin_ip=0; tianjincity=11|110; MUT=09d39ffd-10a9-433a-ae66-643af5eed885; UID=MlwpjR8lR00i62O6Il5FwKYSt59dfwku; gipgeo=34|340

# token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTc4ODE1NzAsInRva2VuIjp7ImxvZ2luVXNlciI6IjEzMTE2NzMwODAxIiwicmFuZG9tU3RyIjoieWgyNmZmMDgxNjE3Mjc2NzcwIn0sImlhdCI6MTYxNzI3Njc3MH0.cGmFI4h8cRB8x_EzJsnY8OCYLxvy3xEGHV-wk2YW8-eWyot3n2e2awGQIeEsWJkCY9iD3itoAOF4-XV4wjee7w; c_id=4301cbc54d2cbe2d58b24a2ec6a3551e18ebf03300e6334c66c2020e818df82a; enc_acc=HRHVbmfRbdAq2IvJ9Nj+ndF7Ha1KYiA52s/VJKcDldmEkrTEjHBGBsHGlop0nJaelfV632qrdrjkqiHE7LHJCEkfJrxqrGrtgDzWUyNKycFNdn1DIR4/kriC/YuIjNkuQSGqmxFsnIGbifPLpoEgpsS4BkypnYNNr3aklagw8YY=; invalid_at=0e37c8b737bf477fe664f76c3485a8ccd1c059e51a9a5643bf3d91f96949662a; random_login=0; t3_token=c62c889f9114886e4b0266c5574b50fb; third_token=eyJkYXRhIjoiMTMyYzJlNGFmOTFiOWU0ZTRmMmMyMDQwOWVkNWU5NDI1NGNjMDliNTgxY2FiOGI3Zjc3YThjNmEyNWY2MTM0ZDBlOTkzM2M2OWY0MThkODcwY2ZlMTFiMDZlMzg1OWVlMjM0YjRhZTY4N2NkYTE5NTQ4NDRiOGE4NDM1NmUwOWMyNGE0NTcyODUxYTdhYzc3YzhiN2M1NjIzYTRiMDcwZiIsInZlcnNpb24iOiIwMCJ9; u_areaCode=360; wo_family=0; u_type=11; c_version=iphone_c@8.0200; channel=GGPD; city=036|360; cw_mutual=7064d003eb3c8934e769e430ecf3d64a91246651671794c1a45e99ee80d5d0db9421693c252fde46ceabfc9e119b26c016ee2c56776f417262d225edaba38f79; devicedId=17B204F6-E3F3-4278-9311-D768200FBC05; ecs_token=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxMzExNjczMDgwMSIsInBybyI6IjAzNiIsImNpdHkiOiIzNjAiLCJpZCI6ImQ2NTcxMjc1ZDk5Y2VjNTBkMTcwYTVmMTgyNTcwMjk0In0.k2Vzc2JiQ5zeTXZCM9N-xnfL2OwdgjKwwyPLHldw7sU; login_type=01; ecs_acc=; c_mobile=13116730801; u_account=13116730801; ecs_acc=fVvwDIvJNwgvai0IwVWHhJO4jImR0pE25hQPdv/uLsZQKtDrONj0+2kH4SCI1n85TKv490rYGugxqshtKtdx7SV7LROzgsYflSMbeFpbMjNLxfIDDDCjwoZvizSbbywgHWOgniqCjgZQljKthGdOkvDjopWUxLNXHf6Ruy6YBi4=; route=1cb499e1e9387df9f55a2f1c6c297bca; myPrize=27e8cd54f5acd31a5b4119771286747b; clientid=98|0; mobileServiceAll=6bb6b8c3fc75339808d1cc59137f6dda; on_info=b7ebdc40ed1791ad2f844a90b2dc06c5