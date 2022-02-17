from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResult2Message(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeVint(self.player.battle_result)

        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1
        exp_reward = [8, 6, 4]
        token_list = [20,15,10]
        practice_exp_reward = [4, 3, 2] 
        practice_token_list = [10,8,5]
        mvp_exp_reward = [10, 5]
        
        
        if self.player.battle_result == 0:
            result = self.player.result + 1
            starplayer = 5
        if self.player.battle_result == 1:
            result = self.player.result
            starplayer = 1
        if self.player.battle_result == 2:
            result = self.player.result
            starplayer = 5
            
        if starplayer == 5:
            starplayerexperience = mvp_exp_reward[0]
            practice_starplayerexperience = mvp_exp_reward[1]
        else:
            starplayerexperience = 0
            practice_starplayerexperience = 0
                    

        if 0 <= brawler_trophies <= 49:
            win_val = 8
            lose_val = 0
            lose_val2 = 0

        else:
            if 50 <= brawler_trophies <= 99:
                win_val = 8
                lose_val = -1
                lose_val2 = -64

            if 100 <= brawler_trophies <= 199:
                win_val = 8
                lose_val = -2
                lose_val2 = -63

            if 200 <= brawler_trophies <= 299:
                win_val = 8
                lose_val = -3
                lose_val2 = -62

            if 300 <= brawler_trophies <= 399:
                win_val = 8
                lose_val = -4
                lose_val2 = -61

            if 400 <= brawler_trophies <= 499:
                win_val = 8
                lose_val = -5
                lose_val2 = -60

            if 500 <= brawler_trophies <= 599:
                win_val = 8
                lose_val = -6
                lose_val2 = -59

            if 600 <= brawler_trophies <= 699:
                win_val = 8
                lose_val = -7
                lose_val2 = -58

            if 700 <= brawler_trophies <= 799:
                win_val = 8
                lose_val = -8
                lose_val2 = -57

            if 800 <= brawler_trophies <= 899:
                win_val = 7
                lose_val = -9
                lose_val2 = -56

            if 900 <= brawler_trophies <= 999:
                win_val = 6
                lose_val = -10
                lose_val2 = -55

            if 1000 <= brawler_trophies <= 1099:
                win_val = 5
                lose_val = -11
                lose_val2 = -54

            if 1100 <= brawler_trophies <= 1199:
                win_val = 4
                lose_val = -12
                lose_val2 = -53

            if brawler_trophies >= 1200:
                win_val = 3
                lose_val = -12
                lose_val2 = -53

        if self.player.battle_result == 0:
            trophiesinresult = win_val
            if result == 0:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 0
            if result == 1:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 1
            if result == 2:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 0
            if result == 3:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 1
            if result == 4:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 6:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 8:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 0
            if result == 9:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 1
            if result == 10:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 0
            if result == 11:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 1
            if result == 12:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 14:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 16:
                trophies = win_val
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 0
            if result == 17:
                trophies = win_val
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 1
            if result == 18:
                trophies = win_val
                mvpexperience = 0
                experience = 0
                tokens = token_list[0]
                startoken = 0
            if result == 19:
                trophies = win_val
                mvpexperience = 0
                experience = 0
                tokens = token_list[0]
                startoken = 1
            if result == 20:
                trophies = win_val
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 21:
                trophies = win_val
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 22:
                trophies = win_val
                mvpexperience = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 23:
                trophies = win_val
                mvpexperience = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 24:
                trophies = win_val
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 0
            if result == 25:
                trophies = win_val
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 1
            if result == 26:
                trophies = win_val
                mvpexperience = 0
                experience = 0
                tokens = token_list[0]
                startoken = 0
            if result == 27:
                trophies = win_val
                mvpexperience = 0
                experience = 0
                tokens = token_list[0]
                startoken = 1
            if result == 28:
                trophies = win_val
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 29:
                trophies = win_val
                mvpexperience = starplayerexperience
                experience = exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 30:
                trophies = win_val
                mvpexperience = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 31:
                trophies = win_val
                mvpexperience = 0
                experience = 0
                tokens = 0
                startoken = 1
                
            self.player.ThreeVSThree_wins += 1
            self.player.player_experience += experience + mvpexperience
            tokenevent = tokens
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            else: 
                doubledtokens = tokens + tokenevent
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + tokenevent + doubledtokens
            new_trophies = self.player.trophies + trophies
            new_tokens = self.player.brawl_boxes + totaltokens
            new_startokens = self.player.big_boxes + startoken
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'BrawlPassTokens', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            DataBase.replaceValue(self, '3vs3Wins', self.player.ThreeVSThree_wins)
            
        elif self.player.battle_result == 1:
            trophiesinresult = lose_val2
            startoken = 0
            if result == 0:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
            if result == 1:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
            if result == 2:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[2]
            if result == 3:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[2]
            if result == 4:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[2]
                tokens = 0
            if result == 5:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[2]
                tokens = 0
            if result == 6:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 7:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 8:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
            if result == 9:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
            if result == 10:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[2]
            if result == 11:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[2]
            if result == 12:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[2]
                tokens = 0
            if result == 13:
                trophies = 0
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[2]
                tokens = 0
            if result == 14:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 15:
                trophies = 0
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 16:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = exp_reward[2]
                tokens = token_list[2]
            if result == 17:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = exp_reward[2]
                tokens = token_list[2]
            if result == 18:
                trophies = lose_val
                mvpexperience = 0
                experience = 0
                tokens = token_list[2]
            if result == 19:
                trophies = lose_val
                mvpexperience = 0
                experience = 0
                tokens = token_list[2]
            if result == 20:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = exp_reward[2]
                tokens = 0
            if result == 21:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = exp_reward[2]
                tokens = 0
            if result == 22:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = 0
                tokens = 0
            if result == 23:
                trophies = lose_val
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 24:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = exp_reward[2]
                tokens = token_list[2]
            if result == 25:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = exp_reward[2]
                tokens = token_list[2]
            if result == 26:
                trophies = lose_val
                mvpexperience = 0
                experience = 0
                tokens = token_list[2]
            if result == 27:
                trophies = lose_val
                mvpexperience = 0
                experience = 0
                tokens = token_list[2]
            if result == 28:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = exp_reward[2]
                tokens = 0
            if result == 29:
                trophies = lose_val
                mvpexperience = starplayerexperience
                experience = exp_reward[2]
                tokens = 0
            if result == 30:
                trophies = lose_val
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 31:
                trophies = lose_val
                mvpexperience = 0
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience + mvpexperience
            tokenevent = tokens
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            else: 
                doubledtokens = tokens + tokenevent
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + tokenevent + doubledtokens
            new_trophies = self.player.trophies + trophies
            new_tokens = self.player.brawl_boxes + totaltokens
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'BrawlPassTokens', new_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)

        elif self.player.battle_result == 2:
            trophiesinresult = 0
            trophies = 0
            startoken = 0
            if result == 0:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
            if result == 1:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
            if result == 2:
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[1]
            if result == 3:
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[1]
            if result == 4:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
                tokens = 0
            if result == 5:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
                tokens = 0
            if result == 6:
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 7:
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 8:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
            if result == 9:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
            if result == 10:
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[1]
            if result == 11:
                mvpexperience = 0
                experience = 0
                tokens = practice_token_list[1]
            if result == 12:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
                tokens = 0
            if result == 13:
                mvpexperience = practice_starplayerexperience
                experience = practice_exp_reward[1]
                tokens = 0
            if result == 14:
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 15:
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 16:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
                tokens = token_list[1]
            if result == 17:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
                tokens = token_list[1]
            if result == 18:
                mvpexperience = 0
                experience = 0
                tokens = token_list[1]
            if result == 19:
                mvpexperience = 0
                experience = 0
                tokens = token_list[1]
            if result == 20:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
                tokens = 0
            if result == 21:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
                tokens = 0
            if result == 22:
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 23:
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 24:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
                tokens = token_list[1]
            if result == 25:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
                tokens = token_list[1]
            if result == 26:
                mvpexperience = 0
                experience = 0
                tokens = token_list[1]
            if result == 27:
                mvpexperience = 0
                experience = 0
                tokens = token_list[1]
            if result == 28:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
                tokens = 0
            if result == 29:
                mvpexperience = starplayerexperience
                experience = exp_reward[1]
                tokens = 0
            if result == 30:
                mvpexperience = 0
                experience = 0
                tokens = 0
            if result == 31:
                mvpexperience = 0
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience + mvpexperience
            tokenevent = tokens
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            else: 
                doubledtokens = tokens + tokenevent
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + tokenevent + doubledtokens
            new_tokens = self.player.brawl_boxes + totaltokens
            DataBase.replaceValue(self, 'BrawlPassTokens', new_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)

        self.writeVint(tokens) # Tokens Gained
        self.writeVint(trophiesinresult) # Trophies Result
        self.writeVint(1) # Unknown
        self.writeVint(doubledtokens) # Doubled Tokens
        self.writeVint(tokenevent) # Double Token Event
        self.writeVint(remainingtokens) # Token Doubler Remaining
        self.writeVint(1) # ???? 
        self.writeVint(1) # Unknown (Unused Star Token Related???)
        self.writeVint(1) # Championship Level Passed
        self.writeVint(1) # Challenge Reward Type (0 = Star Points, 1 = Star Tokens)
        self.writeVint(1) #Challenge Reward Ammount
        self.writeVint(1) # Championship Losses Left
        self.writeVint(1) # Championship Maximun Losses
        self.writeVint(1) # Coin Shower Event
        self.writeVint(1) # Underdog (But I Didn't Coded Yet)
        self.writeVint(result) # Battle Result Info and Stuff
        self.writeVint(1) # Championship Type
        self.writeVint(1) # Championship Qualified and Unused Star Token (Beta Brawl Pass Stuff?)
        self.writeVint(6) # Battle End Screen Players
        
        self.writeVint(starplayer) # Self Star Player Type
        self.writeVint(16) # Player Brawler 
        self.writeVint(self.player.brawler_id)
        self.writeVint(29) # Player Skin 
        self.writeVint(self.player.skin_id)
        self.writeVint(brawler_trophies) # Your Brawler Trophies
        self.writeVint(1) # Your Power Play Points?
        self.writeVint(10) # Your Brawler Power Level
        bool = True
        self.writeBoolean(bool)
        if bool == True:
            self.writeInt(0) # Your HighID
            self.writeInt(1) # Your LowID
        self.writeString(self.player.name) # Your Name
        self.writeVint(100) # Unknown
        self.writeVint(28000000 + self.player.profile_icon) # Player Profile Icon
        self.writeVint(43000000 + self.player.name_color) # Player Name Color

        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.bot1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot1_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.bot2)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot2_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot3)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot3_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot4)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot4_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)

        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot5)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeString(self.player.bot5_n)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        
        # Experience Array # V7
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(experience) # Normal Experience Ammount
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(mvpexperience) # Star Player Experience Ammount

        # Rank Up and Level Up Bonus Array (v12)
        self.writeVint(0) # Count

        # Trophies and Experience Bars Array # (v18)
        self.writeVint(2) # Count
        self.writeVint(1) # Ranks Milestone ID
        self.writeVint(brawler_trophies) # Brawler Trophies Bar
        self.writeVint(brawler_trophies_for_rank) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Milestone ID
        self.writeVint(self.player.player_experience -experience -mvpexperience) # Total Experience Bar
        self.writeVint(self.player.player_experience -experience -mvpexperience) # ???
        self.player.trophyanimation = trophiesinresult
        self.player.tokenanimation = totaltokens
        
        self.writeScId(28, 0)  # Unknown
        self.writeBoolean(True)  # Play Again
        self.writeInt(0) # v4
        self.writeVint(0) # v5
        self.writeVint(0)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeInt(1)
        for x in range(1):
            # sub_216000
            self.writeVint(1) # count
            for x in range(1):
                 #sub_5537D0
                 self.writeVint(1)
                 self.writeVint(1)
                 self.writeVint(1)
                 self.writeVint(1)
                 self.writeVint(1)
                 self.writeVint(0)
                 self.writeVint(1)
                 self.writeVint(1)
                 self.writeInt(0)
                 self.writeInt(0)
                 self.writeScId(16, 0)
                 self.writeVint(0)
                 self.writeVint(0)