import os
import sys
from modules import db_handler

LEVEL_CAP = 250

badge = {0: '<:Unranked:811634098056724511>',
         1: '<:Rank1:809698158631583768>',
         2: '<:Rank2:809698423229906975>',
         3: '<:Rank3:809698491995258881>',
         4: '<:Rank4:809706633726001162>',
         5: '<:Rank5:809706692727406622>',
         6: '<:Rank6:809706734997864448>',
         7: '<:Rank7:809706833459281920>',
         8: '<:Rank8:809706866527174656>',
         9: '<:Rank9:809706905173098512>',
         10: '<:Rank10:809706978686533673>',
         11: '<:Rank11:809707013100797953>',
         12: '<:Rank12:809707086166229042>',
         13: '<:Rank13:809707120479043636>',
         14: '<:Rank14:809707251598098432>',
         15: '<:Rank15:809707309555122178>',
         16: '<:Rank16:809707354215022602>',
         17: '<:Rank17:809707466262183936>',
         18: '<:Rank18:809707500873449542>',
         19: '<:Rank19:809707537582653441>'}
prestige = '<:Prestige:809707605554495527>'
sys.path.insert(1, os.path.abspath('modules'))


def calculate_rank(id: int):
    user = db_handler.fetch_user(id=id)
    level = user['exp'] // LEVEL_CAP
    rank = level // 10

    temp = ''
    if user['prestige'] > 0:
        pre = prestige * user['prestige']
    else:
        pre = ''
    if rank == 0:
        return [level, str(temp + pre + '')]
    text = temp + pre + badge[rank]

    return [level, str(text)]
