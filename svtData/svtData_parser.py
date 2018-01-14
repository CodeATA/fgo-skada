# -*- coding=utf-8 -*-

import json

with open("raw.txt", "r") as raw:
	master = json.load(raw)
	for svt in master['mstSvt']:
		#id = svt['id']
		#svtFile = str(id) + '.svt'
		path = "json_data/"
		if (svt['collectionNo'] == 0):
			continue
		elif (svt['type'] == 6):
			path = path + "craft_essence/"
		else:
			path = path + "servent/"
		collectionId = svt['collectionNo']
		id = svt['id']
		with open(path+str(collectionId), "w", encoding="utf-8") as target:
			target.write('\'mstSvt\':'+str(svt)+"\n")
			for svtLimit in master['mstSvtLimit']:
				if svtLimit['svtId'] == id and svtLimit['limitCount'] == 4:
					target.write('\'mstSvtLimit\':'+str(svtLimit)+"\n")
			
			target.write("\n")
			for svtTreasureDevice in master['mstSvtTreasureDevice']:
				if svtTreasureDevice['svtId'] == id and svtTreasureDevice['treasureDeviceId'] != 100:
					target.write('\'mstSvtTreasureDevice\':'+str(svtTreasureDevice)+"\n")
					for treasureDeviceLv in master['mstTreasureDeviceLv']:
						if treasureDeviceLv['treaureDeviceId'] == svtTreasureDevice['treasureDeviceId']:
							target.write('\'mstTreasureDeviceLv\':'+str(treasureDeviceLv)+"\n")
					for treasureDevice in master['mstTreasureDevice']:
						if treasureDevice['id'] == svtTreasureDevice['treasureDeviceId']:
							target.write('\'mstTreasureDevice\':'+str(treasureDevice)+"\n")
					for treasureDeviceDetail in master['mstTreasureDeviceDetail']:
						if treasureDeviceDetail['id'] == svtTreasureDevice['treasureDeviceId']:
							target.write('\'mstTreasureDeviceDetail\':'+str(treasureDeviceDetail)+"\n")
			
			target.write("\n")
			for svtSkill in master['mstSvtSkill']:
				if svtSkill['svtId'] == id:
					target.write('\'mstSvtSkill\':'+str(svtSkill)+"\n")
					for skill in master['mstSkill']:
						if skill['id'] == svtSkill['skillId']:
							target.write('\'mstSkill\':'+str(skill)+"\n")
			
			target.write("\nclassPassive:\n")
			for classPassive in svt['classPassive']:
				for passive in master['mstSkill']:
					if passive['id'] == classPassive:
						target.write(str(passive)+"\n")
				for skillDetail in master['mstSkillDetail']:
					if skillDetail['id'] == classPassive:
						target.write(str(skillDetail)+"\n")