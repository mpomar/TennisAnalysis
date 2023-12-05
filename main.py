from data_processing import stats_comparison, elo_comparison, wc_reminder
import scraper
from scraper import driver
import time

# Prompt the user to enter the initial inputs
player1 = input("Enter the name of Player 1: ")
wc_player1 = input("Is Player 1 a Wildcard / Qualifier? [Y/N] ")
player2 = input("Enter the name of Player 2: ")
wc_player2 = input("Is Player 2 a Wildcard / Qualifier? [Y/N] ")
surface = input("On what surface they will play? [Clay, Hard, Grass] ")
print()

# Create variations of the initial inputs
conca_player1 = player1.replace(' ', '')
conca_player2 = player2.replace(' ', '')
nbsp_player1 = player1.replace(' ', ' ')
nbsp_player2 = player2.replace(' ', ' ')

stats_comparison(conca_player1, conca_player2, player1, player2, nbsp_player1, nbsp_player2, surface) # this controls Match comparison & RPW/SPW
elo_comparison(nbsp_player1, nbsp_player2, surface, player1, player2) # this controls Raw Elo for the defined surface & Peak Match
wc_players = wc_reminder(wc_player1, wc_player2) # this controls the Wildcard / Qualifier
print(wc_players)
print()

# For completion provide full Player 1 overview
print(f"{player1} Overview")
print()
player_stats = scraper.scrape_player_data(conca_player1)
print(player_stats)
print()
player_elo = scraper.scrape_player_elo(nbsp_player1)
print(player_elo)

time.sleep(2)
print()

# For completion provide full Player 2 overview
print(f"{player2} Overview")
print()
player_stats = scraper.scrape_player_data(conca_player2)
print(player_stats)
print()
player_elo = scraper.scrape_player_elo(nbsp_player2)
print(player_elo)

driver.quit()