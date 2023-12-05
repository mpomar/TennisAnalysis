import scraper
from scraper import driver
import time

def stats_comparison(conca_player1, conca_player2, player1, player2, nbsp_player1, nbsp_player2, surface):
    # Scrape player stats
    time.sleep(3)
    p1_stats = scraper.scrape_player_data(conca_player1)
    p2_stats = scraper.scrape_player_data(conca_player2)

    p1_match = p1_stats["Match"].iloc[0]
    p1_matchpercentage = p1_match[-4:-2]
    p2_match = p2_stats["Match"].iloc[0]
    p2_matchpercentage = p2_match[-4:-2]

    p1_SPW = float(p1_stats["SPW"].iloc[0].strip('%')) / 100
    p1_RPW = float(p1_stats["RPW"].iloc[0].strip('%')) / 100
    p2_SPW = float(p2_stats["SPW"].iloc[0].strip('%')) / 100
    p2_RPW = float(p2_stats["RPW"].iloc[0].strip('%')) / 100
    p1_power = p1_RPW / p2_SPW
    p2_power = p2_RPW / p1_SPW

    # Compare Match percentage of the two players for the current year
    if p1_matchpercentage > p2_matchpercentage:
        print(f"{player1} has the best Match percentage for the current year: {p1_match} vs {p2_match}")
    else:
        print(f"{player2} has the best Match percentage for the current year: {p1_match} vs {p2_match}")

    # Compare RPW/SPW power of the two players
    if p1_power > p2_power:
        print(f"{player1} has the best RPW/SPW ratio: {p1_power} vs {p2_power}")
    else:
        print(f"{player2} has the best RPW/SPW ratio: {p1_power} vs {p2_power}")

def elo_comparison(nbsp_player1, nbsp_player2, surface, player1, player2):
    # Scrape from the Elo table
    time.sleep(3)
    p1_elo = scraper.scrape_player_elo(nbsp_player1)
    p2_elo = scraper.scrape_player_elo(nbsp_player2)

    # Get the correct surface value for player 1
    if surface == "Clay":
        p1_surface_elo = p1_elo["ClayRaw"]
    elif surface == "Hard":
        p1_surface_elo = p1_elo["HardRaw"]
    elif surface == "Grass":
        p1_surface_elo = p1_elo["GrassRaw"]
    else:
        print("Invalid surface value")

    # Get the correct surface value for player 2
    if surface == "Clay":
        p2_surface_elo = p2_elo["ClayRaw"]
    elif surface == "Hard":
        p2_surface_elo = p2_elo["HardRaw"]
    elif surface == "Grass":
        p2_surface_elo = p2_elo["GrassRaw"]
    else:
        print("Invalid surface value")

    # Compare the Elo of the two players
    if p1_surface_elo.iloc[0] > p2_surface_elo.iloc[0]:
        print(f"{player1} has the highest Elo on {surface}: {p1_surface_elo.iloc[0]} vs {p2_surface_elo.iloc[0]}")
    else:
        print(f"{player2} has the highest Elo on {surface}: {p1_surface_elo.iloc[0]} vs {p2_surface_elo.iloc[0]}")

    # Get the Peak Match of the two players
    p1_elo = scraper.scrape_player_elo(nbsp_player1)
    p1_peakmatch = p1_elo["Peak Match"].iloc[0]
    p1_peakmatch = p1_peakmatch[:4]

    p2_elo = scraper.scrape_player_elo(nbsp_player2)
    p2_peakmatch = p2_elo["Peak Match"].iloc[0]
    p2_peakmatch = p2_peakmatch[:4]

    # Compare the Peak Match of the two players
    if p1_peakmatch > p2_peakmatch:
        print(f"{player1} has the most recent peak match: {p1_peakmatch} vs {p2_peakmatch}")
    elif p2_peakmatch > p1_peakmatch:
        print(f"{player2} has the most recent peak match: {p1_peakmatch} vs {p2_peakmatch}")
    else:
        print("Peak Match cannot be considered, both players have the same year")

def wc_reminder(wc_player1: str, wc_player2: str) -> str:
    if wc_player1 == 'Y' and wc_player2 == 'Y':
        return "Both players are either a Wildcard or Qualifier"
    elif wc_player1 == 'N' and wc_player2 == 'N':
        return "No Wildcards or Qualifiers"
    else:
        wildcard_player = "Player 1" if wc_player1 == 'Y' else "Player 2"
        return f"{wildcard_player} either qualified or has received a wildcard"