from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class BattleResultMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(2) # Battle Result Type

        self.writeVint(self.player.rank) # Rank Score

        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1
        exp_reward = [15, 12, 9, 6, 5, 4, 3, 2, 1, 0]
        token_list = [34, 28, 22, 16, 12, 8, 6, 4, 2, 0]
        practice_exp_reward = [8, 6, 5, 3, 3, 2, 2, 1, 1, 0] 
        practice_token_list = [17, 14, 11, 8, 6, 4, 3, 2, 1, 0]
        if 1 <= self.player.rank <= 4:
            result = self.player.result + 1
        if self.player.rank >= 5:
            result = self.player.result

        if 0 <= brawler_trophies <= 49:
            win = 8
            rank_1_val = 10
            rank_2_val = 8
            rank_3_val = 7
            rank_4_val = 6
            rank_5_val = 4
            rank_6_val = 2
            rank_7_val = 2
            rank_8_val = 1
            rank_9_val = 0
            rank_10_val = 0

            rank_1_val2 = 10
            rank_2_val2 = 8
            rank_3_val2 = 7
            rank_4_val2 = 6
            rank_5_val2 = 4
            rank_6_val2 = 2
            rank_7_val2 = 2
            rank_8_val2 = 1
            rank_9_val2 = 0
            rank_10_val2 = 0

        else:
            if 50 <= brawler_trophies <= 99:
                win = 7
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 3
                rank_6_val = 2
                rank_7_val = 2
                rank_8_val = 0
                rank_9_val = -1
                rank_10_val = -2

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 7
                rank_4_val2 = 6
                rank_5_val2 = 3
                rank_6_val2 = 2
                rank_7_val2 = 2
                rank_8_val2 = 0
                rank_9_val2 = -64
                rank_10_val2 = -63

            if 100 <= brawler_trophies <= 199:
                win = 6
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 3
                rank_6_val = 1
                rank_7_val = 0
                rank_8_val = -1
                rank_9_val = -2
                rank_10_val = -2

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 7
                rank_4_val2 = 6
                rank_5_val2 = 3
                rank_6_val2 = 1
                rank_7_val2 = 0
                rank_8_val2 = -64
                rank_9_val2 = -63
                rank_10_val2 = -63

            if 200 <= brawler_trophies <= 299:
                win = 6
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 3
                rank_6_val = 1
                rank_7_val = 0
                rank_8_val = -2
                rank_9_val = -3
                rank_10_val = -3

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 6
                rank_4_val2 = 5
                rank_5_val2 = 3
                rank_6_val2 = 1
                rank_7_val2 = 0
                rank_8_val2 = -63
                rank_9_val2 = -62
                rank_10_val2 = -62

            if 300 <= brawler_trophies <= 399:
                win = 5
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 2
                rank_6_val = 0
                rank_7_val = 0
                rank_8_val = -3
                rank_9_val = -4
                rank_10_val = -4

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 6
                rank_4_val2 = 5
                rank_5_val2 = 2
                rank_6_val2 = 0
                rank_7_val2 = 0
                rank_8_val2 = -62
                rank_9_val2 = -61
                rank_10_val2 = -61

            if 400 <= brawler_trophies <= 499:
                win = 5
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 2
                rank_6_val = -1
                rank_7_val = -2
                rank_8_val = -3
                rank_9_val = -5
                rank_10_val = -5

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 6
                rank_4_val2 = 5
                rank_5_val2 = 2
                rank_6_val2 = -64
                rank_7_val2 = -63
                rank_8_val2 = -62
                rank_9_val2 = -60
                rank_10_val2 = -60

            if 500 <= brawler_trophies <= 599:
                win = 5
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 2
                rank_6_val = -1
                rank_7_val = -2
                rank_8_val = -5
                rank_9_val = -6
                rank_10_val = -6

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 6
                rank_4_val2 = 4
                rank_5_val2 = 2
                rank_6_val2 = -64
                rank_7_val2 = -63
                rank_8_val2 = -60
                rank_9_val2 = -59
                rank_10_val2 = -59

            if 600 <= brawler_trophies <= 699:
                win = 5
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 1
                rank_6_val = -2
                rank_7_val = -2
                rank_8_val = -5
                rank_9_val = -7
                rank_10_val = -8

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 6
                rank_4_val2 = 4
                rank_5_val2 = 1
                rank_6_val2 = -63
                rank_7_val2 = -63
                rank_8_val2 = -60
                rank_9_val2 = -58
                rank_10_val2 = -57

            if 700 <= brawler_trophies <= 799:
                win = 5
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 1
                rank_6_val = -3
                rank_7_val = -4
                rank_8_val = -5
                rank_9_val = -8
                rank_10_val = -9

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 6
                rank_4_val2 = 4
                rank_5_val2 = 1
                rank_6_val2 = -62
                rank_7_val2 = -61
                rank_8_val2 = -60
                rank_9_val2 = -57
                rank_10_val2 = -56

            if 800 <= brawler_trophies <= 899:
                win = 4
                rank_1_val = 9
                rank_2_val = 7
                rank_3_val = 5
                rank_4_val = 2
                rank_5_val = 0
                rank_6_val = -3
                rank_7_val = -4
                rank_8_val = -7
                rank_9_val = -9
                rank_10_val = -10

                rank_1_val2 = 9
                rank_2_val2 = 7
                rank_3_val2 = 5
                rank_4_val2 = 2
                rank_5_val2 = 0
                rank_6_val2 = -62
                rank_7_val2 = -61
                rank_8_val2 = -58
                rank_9_val2 = -56
                rank_10_val2 = -55

            if 900 <= brawler_trophies <= 999:
                win = 4
                rank_1_val = 8
                rank_2_val = 6
                rank_3_val = 4
                rank_4_val = 1
                rank_5_val = -1
                rank_6_val = -3
                rank_7_val = -6
                rank_8_val = -8
                rank_9_val = -10
                rank_10_val = -11

                rank_1_val2 = 8
                rank_2_val2 = 6
                rank_3_val2 = 4
                rank_4_val2 = 1
                rank_5_val2 = -64
                rank_6_val2 = -62
                rank_7_val2 = -59
                rank_8_val2 = -57
                rank_9_val2 = -55
                rank_10_val2 = -54

            if 1000 <= brawler_trophies <= 1099:
                win = 4
                rank_1_val = 6
                rank_2_val = 5
                rank_3_val = 3
                rank_4_val = 1
                rank_5_val = -2
                rank_6_val = -5
                rank_7_val = -6
                rank_8_val = -9
                rank_9_val = -11
                rank_10_val = -12

                rank_1_val2 = 6
                rank_2_val2 = 5
                rank_3_val2 = 3
                rank_4_val2 = 1
                rank_5_val2 = -63
                rank_6_val2 = -60
                rank_7_val2 = -59
                rank_8_val2 = -56
                rank_9_val2 = -54
                rank_10_val2 = -53

            if 1100 <= brawler_trophies <= 1199:
                win = 3
                rank_1_val = 5
                rank_2_val = 4
                rank_3_val = 1
                rank_4_val = 0
                rank_5_val = -2
                rank_6_val = -6
                rank_7_val = -7
                rank_8_val = -10
                rank_9_val = -12
                rank_10_val = -13

                rank_1_val2 = 5
                rank_2_val2 = 4
                rank_3_val2 = 1
                rank_4_val2 = 0
                rank_5_val2 = -63
                rank_6_val2 = -59
                rank_7_val2 = -58
                rank_8_val2 = -55
                rank_9_val2 = -53
                rank_10_val2 = -52

            if brawler_trophies >= 1200:
                win = 2
                rank_1_val = 5
                rank_2_val = 3
                rank_3_val = 0
                rank_4_val = -1
                rank_5_val = -2
                rank_6_val = -6
                rank_7_val = -8
                rank_8_val = -11
                rank_9_val = -12
                rank_10_val = -13

                rank_1_val2 = 5
                rank_2_val2 = 3
                rank_3_val2 = 0
                rank_4_val2 = -64
                rank_5_val2 = -63
                rank_6_val2 = -59
                rank_7_val2 = -57
                rank_8_val2 = -54
                rank_9_val2 = -53
                rank_10_val2 = -52

        if self.player.rank == 1:
            trophiesinresult = rank_1_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 0
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 1
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 1
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = practice_token_list[0]
                startoken = 1
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[0]
                startoken = 1
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 16:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 0
            if result == 17:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 1
            if result == 18:
                trophies = rank_1_val
                experience = 0
                tokens = token_list[0]
                startoken = 0
            if result == 19:
                trophies = rank_1_val
                experience = 0
                tokens = token_list[0]
                startoken = 1
            if result == 20:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 21:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 22:
                trophies = rank_1_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 23:
                trophies = rank_1_val
                experience = 0
                tokens = 0
                startoken = 1
            if result == 24:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 0
            if result == 25:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = token_list[0]
                startoken = 1
            if result == 26:
                trophies = rank_1_val
                experience = 0
                tokens = token_list[0]
                startoken = 0
            if result == 27:
                trophies = rank_1_val
                experience = 0
                tokens = token_list[0]
                startoken = 1
            if result == 28:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = 0
                startoken = 0
            if result == 29:
                trophies = rank_1_val
                experience = exp_reward[0]
                tokens = 0
                startoken = 1
            if result == 30:
                trophies = rank_1_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 31:
                trophies = rank_1_val
                experience = 0
                tokens = 0
                startoken = 1
                
            self.player.solo_wins += 1
            self.player.player_experience += experience
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
            DataBase.replaceValue(self, 'soloWins', self.player.solo_wins)
            
        if self.player.rank == 2:
            trophiesinresult = rank_2_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
                startoken = 0
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
                startoken = 1
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[1]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[1]
                startoken = 1
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = 0
                startoken = 1
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = practice_token_list[1]
                startoken = 1
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[1]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[1]
                startoken = 1
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[1]
                tokens = 0
                startoken = 1
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 16:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = token_list[1]
                startoken = 0
            if result == 17:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = token_list[1]
                startoken = 1
            if result == 18:
                trophies = rank_2_val
                experience = 0
                tokens = token_list[1]
                startoken = 0
            if result == 19:
                trophies = rank_2_val
                experience = 0
                tokens = token_list[1]
                startoken = 1
            if result == 20:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = 0
                startoken = 0
            if result == 21:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = 0
                startoken = 1
            if result == 22:
                trophies = rank_2_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 23:
                trophies = rank_2_val
                experience = 0
                tokens = 0
                startoken = 1
            if result == 24:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = token_list[1]
                startoken = 0
            if result == 25:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = token_list[1]
                startoken = 1
            if result == 26:
                trophies = rank_2_val
                experience = 0
                tokens = token_list[1]
                startoken = 0
            if result == 27:
                trophies = rank_2_val
                experience = 0
                tokens = token_list[1]
                startoken = 1
            if result == 28:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = 0
                startoken = 0
            if result == 29:
                trophies = rank_2_val
                experience = exp_reward[1]
                tokens = 0
                startoken = 1
            if result == 30:
                trophies = rank_2_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 31:
                trophies = rank_2_val
                experience = 0
                tokens = 0
                startoken = 1
                
            self.player.player_experience += experience
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
            
        if self.player.rank == 3:
            trophiesinresult = rank_3_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
                startoken = 0
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
                startoken = 1
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[2]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[2]
                startoken = 1
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = 0
                startoken = 1
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = practice_token_list[2]
                startoken = 1
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[2]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[2]
                startoken = 1
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[2]
                tokens = 0
                startoken = 1
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 16:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = token_list[2]
                startoken = 0
            if result == 17:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = token_list[2]
                startoken = 1
            if result == 18:
                trophies = rank_3_val
                experience = 0
                tokens = token_list[2]
                startoken = 0
            if result == 19:
                trophies = rank_3_val
                experience = 0
                tokens = token_list[2]
                startoken = 1
            if result == 20:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = 0
                startoken = 0
            if result == 21:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = 0
                startoken = 1
            if result == 22:
                trophies = rank_3_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 23:
                trophies = rank_3_val
                experience = 0
                tokens = 0
                startoken = 1
            if result == 24:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = token_list[2]
                startoken = 0
            if result == 25:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = token_list[2]
                startoken = 1
            if result == 26:
                trophies = rank_3_val
                experience = 0
                tokens = token_list[2]
                startoken = 0
            if result == 27:
                trophies = rank_3_val
                experience = 0
                tokens = token_list[2]
                startoken = 1
            if result == 28:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = 0
                startoken = 0
            if result == 29:
                trophies = rank_3_val
                experience = exp_reward[2]
                tokens = 0
                startoken = 1
            if result == 30:
                trophies = rank_3_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 31:
                trophies = rank_3_val
                experience = 0
                tokens = 0
                startoken = 1
                
            self.player.player_experience += experience
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
            
        if self.player.rank == 4:
            trophiesinresult = rank_4_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = practice_token_list[3]
                startoken = 0
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = practice_token_list[3]
                startoken = 1
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[3]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[3]
                startoken = 1
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = 0
                startoken = 1
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = practice_token_list[3]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = practice_token_list[3]
                startoken = 1
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[3]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[3]
                startoken = 1
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[3]
                tokens = 0
                startoken = 1
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 1
            if result == 16:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = token_list[3]
                startoken = 0
            if result == 17:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = token_list[3]
                startoken = 1
            if result == 18:
                trophies = rank_4_val
                experience = 0
                tokens = token_list[3]
                startoken = 0
            if result == 19:
                trophies = rank_4_val
                experience = 0
                tokens = token_list[3]
                startoken = 1
            if result == 20:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = 0
                startoken = 0
            if result == 21:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = 0
                startoken = 1
            if result == 22:
                trophies = rank_4_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 23:
                trophies = rank_4_val
                experience = 0
                tokens = 0
                startoken = 1
            if result == 24:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = token_list[3]
                startoken = 0
            if result == 25:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = token_list[3]
                startoken = 1
            if result == 26:
                trophies = rank_4_val
                experience = 0
                tokens = token_list[3]
                startoken = 0
            if result == 27:
                trophies = rank_4_val
                experience = 0
                tokens = token_list[3]
                startoken = 1
            if result == 28:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = 0
                startoken = 0
            if result == 29:
                trophies = rank_4_val
                experience = exp_reward[3]
                tokens = 0
                startoken = 1
            if result == 30:
                trophies = rank_4_val
                experience = 0
                tokens = 0
                startoken = 0
            if result == 31:
                trophies = rank_4_val
                experience = 0
                tokens = 0
                startoken = 1
                
            self.player.player_experience += experience
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
            
        if self.player.rank == 5:
            startoken = 0
            trophiesinresult = rank_5_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[4]
                tokens = practice_token_list[4]
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[4]
                tokens = practice_token_list[4]
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[4]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[4]
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[4]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[4]
                tokens = 0
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[4]
                tokens = practice_token_list[4]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[4]
                tokens = practice_token_list[4]
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[4]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[4]
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[4]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[4]
                tokens = 0
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 16:
                trophies = rank_5_val
                experience = exp_reward[4]
                tokens = token_list[4]
            if result == 17:
                trophies = rank_5_val
                experience = exp_reward[4]
                tokens = token_list[4]
            if result == 18:
                trophies = rank_5_val
                experience = 0
                tokens = token_list[4]
            if result == 19:
                trophies = rank_5_val
                experience = 0
                tokens = token_list[4]
            if result == 20:
                trophies = rank_5_val
                experience = exp_reward[4]
                tokens = 0
            if result == 21:
                trophies = rank_5_val
                experience = exp_reward[4]
                tokens = 0
            if result == 22:
                trophies = rank_5_val
                experience = 0
                tokens = 0
            if result == 23:
                trophies = rank_5_val
                experience = 0
                tokens = 0
            if result == 24:
                trophies = rank_5_val
                experience = exp_reward[4]
                tokens = token_list[4]
            if result == 25:
                trophies = rank_5_val
                experience = exp_reward[4]
                tokens = token_list[4]
            if result == 26:
                trophies = rank_5_val
                experience = 0
                tokens = token_list[4]
            if result == 27:
                trophies = rank_5_val
                experience = 0
                tokens = token_list[4]
            if result == 28:
                trophies = rank_5_val
                experience = exp_reward[4]
                tokens = 0
            if result == 29:
                trophies = rank_5_val
                experience = exp_reward[4]
                tokens = 0
            if result == 30:
                trophies = rank_5_val
                experience = 0
                tokens = 0
            if result == 31:
                trophies = rank_5_val
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience
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
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'BrawlPassTokens', new_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            
        if self.player.rank == 6:
            startoken = 0
            trophiesinresult = rank_6_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[5]
                tokens = practice_token_list[5]
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[5]
                tokens = practice_token_list[5]
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[5]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[5]
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[5]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[5]
                tokens = 0
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[5]
                tokens = practice_token_list[5]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[5]
                tokens = practice_token_list[5]
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[5]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[5]
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[5]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[5]
                tokens = 0
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 16:
                trophies = rank_6_val
                experience = exp_reward[5]
                tokens = token_list[5]
            if result == 17:
                trophies = rank_6_val
                experience = exp_reward[5]
                tokens = token_list[5]
            if result == 18:
                trophies = rank_6_val
                experience = 0
                tokens = token_list[5]
            if result == 19:
                trophies = rank_6_val
                experience = 0
                tokens = token_list[5]
            if result == 20:
                trophies = rank_6_val
                experience = exp_reward[5]
                tokens = 0
            if result == 21:
                trophies = rank_6_val
                experience = exp_reward[5]
                tokens = 0
            if result == 22:
                trophies = rank_6_val
                experience = 0
                tokens = 0
            if result == 23:
                trophies = rank_6_val
                experience = 0
                tokens = 0
            if result == 24:
                trophies = rank_6_val
                experience = exp_reward[5]
                tokens = token_list[5]
            if result == 25:
                trophies = rank_6_val
                experience = exp_reward[5]
                tokens = token_list[5]
            if result == 26:
                trophies = rank_6_val
                experience = 0
                tokens = token_list[5]
            if result == 27:
                trophies = rank_6_val
                experience = 0
                tokens = token_list[5]
            if result == 28:
                trophies = rank_6_val
                experience = exp_reward[5]
                tokens = 0
            if result == 29:
                trophies = rank_6_val
                experience = exp_reward[5]
                tokens = 0
            if result == 30:
                trophies = rank_6_val
                experience = 0
                tokens = 0
            if result == 31:
                trophies = rank_6_val
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience
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
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'BrawlPassTokens', new_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            
        if self.player.rank == 7:
            startoken = 0
            trophiesinresult = rank_7_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[6]
                tokens = practice_token_list[6]
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[6]
                tokens = practice_token_list[6]
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[6]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[6]
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[6]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[6]
                tokens = 0
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[6]
                tokens = practice_token_list[6]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[6]
                tokens = practice_token_list[6]
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[6]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[6]
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[6]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[6]
                tokens = 0
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 16:
                trophies = rank_7_val
                experience = exp_reward[6]
                tokens = token_list[6]
            if result == 17:
                trophies = rank_7_val
                experience = exp_reward[6]
                tokens = token_list[6]
            if result == 18:
                trophies = rank_7_val
                experience = 0
                tokens = token_list[6]
            if result == 19:
                trophies = rank_7_val
                experience = 0
                tokens = token_list[6]
            if result == 20:
                trophies = rank_7_val
                experience = exp_reward[6]
                tokens = 0
            if result == 21:
                trophies = rank_7_val
                experience = exp_reward[6]
                tokens = 0
            if result == 22:
                trophies = rank_7_val
                experience = 0
                tokens = 0
            if result == 23:
                trophies = rank_7_val
                experience = 0
                tokens = 0
            if result == 24:
                trophies = rank_7_val
                experience = exp_reward[6]
                tokens = token_list[6]
            if result == 25:
                trophies = rank_7_val
                experience = exp_reward[6]
                tokens = token_list[6]
            if result == 26:
                trophies = rank_7_val
                experience = 0
                tokens = token_list[6]
            if result == 27:
                trophies = rank_7_val
                experience = 0
                tokens = token_list[6]
            if result == 28:
                trophies = rank_7_val
                experience = exp_reward[6]
                tokens = 0
            if result == 29:
                trophies = rank_7_val
                experience = exp_reward[6]
                tokens = 0
            if result == 30:
                trophies = rank_7_val
                experience = 0
                tokens = 0
            if result == 31:
                trophies = rank_7_val
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience
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
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'BrawlPassTokens', new_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            
        if self.player.rank == 8:
            startoken = 0
            trophiesinresult = rank_8_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[7]
                tokens = practice_token_list[7]
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[7]
                tokens = practice_token_list[7]
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[7]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[7]
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[7]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[7]
                tokens = 0
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[7]
                tokens = practice_token_list[7]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[7]
                tokens = practice_token_list[7]
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[7]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[7]
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[7]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[7]
                tokens = 0
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 16:
                trophies = rank_8_val
                experience = exp_reward[7]
                tokens = token_list[7]
            if result == 17:
                trophies = rank_8_val
                experience = exp_reward[7]
                tokens = token_list[7]
            if result == 18:
                trophies = rank_8_val
                experience = 0
                tokens = token_list[7]
            if result == 19:
                trophies = rank_8_val
                experience = 0
                tokens = token_list[7]
            if result == 20:
                trophies = rank_8_val
                experience = exp_reward[7]
                tokens = 0
            if result == 21:
                trophies = rank_8_val
                experience = exp_reward[7]
                tokens = 0
            if result == 22:
                trophies = rank_8_val
                experience = 0
                tokens = 0
            if result == 23:
                trophies = rank_8_val
                experience = 0
                tokens = 0
            if result == 24:
                trophies = rank_8_val
                experience = exp_reward[7]
                tokens = token_list[7]
            if result == 25:
                trophies = rank_8_val
                experience = exp_reward[7]
                tokens = token_list[7]
            if result == 26:
                trophies = rank_8_val
                experience = 0
                tokens = token_list[7]
            if result == 27:
                trophies = rank_8_val
                experience = 0
                tokens = token_list[7]
            if result == 28:
                trophies = rank_8_val
                experience = exp_reward[7]
                tokens = 0
            if result == 29:
                trophies = rank_8_val
                experience = exp_reward[7]
                tokens = 0
            if result == 30:
                trophies = rank_8_val
                experience = 0
                tokens = 0
            if result == 31:
                trophies = rank_8_val
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience
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
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'BrawlPassTokens', new_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
                
        if self.player.rank == 9:
            startoken = 0
            trophiesinresult = rank_9_val2
            if result == 0:
                trophies = 0
                experience = practice_exp_reward[8]
                tokens = practice_token_list[8]
            if result == 1:
                trophies = 0
                experience = practice_exp_reward[8]
                tokens = practice_token_list[8]
            if result == 2:
                trophies = 0
                experience = 0
                tokens = practice_token_list[8]
                startoken = 0
            if result == 3:
                trophies = 0
                experience = 0
                tokens = practice_token_list[8]
            if result == 4:
                trophies = 0
                experience = practice_exp_reward[8]
                tokens = 0
                startoken = 0
            if result == 5:
                trophies = 0
                experience = practice_exp_reward[8]
                tokens = 0
            if result == 6:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 7:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 8:
                trophies = 0
                experience = practice_exp_reward[8]
                tokens = practice_token_list[8]
                startoken = 0
            if result == 9:
                trophies = 0
                experience = practice_exp_reward[8]
                tokens = practice_token_list[8]
            if result == 10:
                trophies = 0
                experience = 0
                tokens = practice_token_list[8]
                startoken = 0
            if result == 11:
                trophies = 0
                experience = 0
                tokens = practice_token_list[8]
            if result == 12:
                trophies = 0
                experience = practice_exp_reward[8]
                tokens = 0
                startoken = 0
            if result == 13:
                trophies = 0
                experience = practice_exp_reward[8]
                tokens = 0
            if result == 14:
                trophies = 0
                experience = 0
                tokens = 0
                startoken = 0
            if result == 15:
                trophies = 0
                experience = 0
                tokens = 0
            if result == 16:
                trophies = rank_9_val
                experience = exp_reward[8]
                tokens = token_list[8]
            if result == 17:
                trophies = rank_9_val
                experience = exp_reward[8]
                tokens = token_list[8]
            if result == 18:
                trophies = rank_9_val
                experience = 0
                tokens = token_list[8]
            if result == 19:
                trophies = rank_9_val
                experience = 0
                tokens = token_list[8]
            if result == 20:
                trophies = rank_9_val
                experience = exp_reward[8]
                tokens = 0
            if result == 21:
                trophies = rank_9_val
                experience = exp_reward[8]
                tokens = 0
            if result == 22:
                trophies = rank_9_val
                experience = 0
                tokens = 0
            if result == 23:
                trophies = rank_9_val
                experience = 0
                tokens = 0
            if result == 24:
                trophies = rank_9_val
                experience = exp_reward[8]
                tokens = token_list[8]
            if result == 25:
                trophies = rank_9_val
                experience = exp_reward[8]
                tokens = token_list[8]
            if result == 26:
                trophies = rank_9_val
                experience = 0
                tokens = token_list[8]
            if result == 27:
                trophies = rank_9_val
                experience = 0
                tokens = token_list[8]
            if result == 28:
                trophies = rank_9_val
                experience = exp_reward[8]
                tokens = 0
            if result == 29:
                trophies = rank_9_val
                experience = exp_reward[8]
                tokens = 0
            if result == 30:
                trophies = rank_9_val
                experience = 0
                tokens = 0
            if result == 31:
                trophies = rank_9_val
                experience = 0
                tokens = 0
                
            self.player.player_experience += experience
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
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            DataBase.replaceValue(self, 'BrawlPassTokens', new_tokens)
            DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)
            
        if self.player.rank == 10:
            startoken = 0
            experience = 0
            tokens = 0
            trophiesinresult = rank_10_val2
            if 0 <= result <= 15:
                trophies = 0
            if 16 <= result <= 31:
                trophies = rank_10_val
            
            tokenevent = tokens
            if self.player.tokensdoubler <= 0:
                doubledtokens = 0
            else: 
                doubledtokens = tokens + tokenevent
            remainingtokens = (self.player.tokensdoubler) - doubledtokens
            totaltokens = tokens + tokenevent + doubledtokens  
            new_trophies = self.player.trophies + trophies
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
            if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
                self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank + trophies
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
            DataBase.replaceValue(self, 'trophies', new_trophies)

        self.writeVint(tokens) # Tokens Gained
        self.writeVint(trophiesinresult) # Trophies Result
        self.writeVint(0) # Unknown
        self.writeVint(doubledtokens) # Doubled Tokens
        self.writeVint(tokenevent) # Double Token Event
        self.writeVint(remainingtokens) # Token Doubler Remaining
        self.writeVint(3) # Championship Lose 
        self.writeVint(0) # Unknown
        self.writeVint(2) # Championship Level Passed
        self.writeVint(0) # Challenge Reward Type (0 = Star Tokens, 1 = Star Tokens)
        self.writeVint(100) #C hallenge Reward Ammount
        self.writeVint(3) # Championship Losses Left
        self.writeVint(3) # Championship Maximun Losses
        self.writeVint(0) # Coin Shower Event
        self.writeVint(0) #Underdog (But I Didn't Coded Yet)
        self.writeVint(16) #  Battle Result Info and Stuff
        self.writeVint(0) # Championship Type
        self.writeVint(0) # Unused Star Token (Beta Brawl Pass Stuff?)
        self.writeVint(1) # Battle End Screen Players
        
        self.writeVint(1) # Self Star Player Type
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

        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(experience) # Normal Experience Ammount
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(0) # Star Player Experience Ammount

        # Rank Up and Level Up Bonus Array
        self.writeVint(0) # Count

        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Ranks Milestone ID
        self.writeVint(brawler_trophies) # Brawler Trophies Bar
        self.writeVint(brawler_trophies_for_rank) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Milestone ID
        self.writeVint(self.player.player_experience -experience) # Total Experience Bar
        self.writeVint(self.player.player_experience -experience) # ???
        self.player.trophyanimation = trophiesinresult
        self.player.tokenanimation = totaltokens
        
        self.writeVint(0)  # Unknown
        self.writeBoolean(True)  # Play Again
