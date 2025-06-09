#!/usr/bin/env python3
import os
import csv

from sportsradar_client import (
    get_season_game_ids,
    API_KEY,
    ACCESS_LEVEL,
    LANGUAGE,
    SEASON_YEAR,
    SEASON_TYPE,
    FORMAT,
)

def main():
    assets_dir = "assets"
    os.makedirs(assets_dir, exist_ok=True)
    game_ids = get_season_game_ids(
        API_KEY, ACCESS_LEVEL, LANGUAGE, SEASON_YEAR, SEASON_TYPE, FORMAT
    )
    csv_path = os.path.join(assets_dir, "game_ids.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["game_id"])
        for gid in game_ids:
            writer.writerow([gid])
    print(f"Wrote {len(game_ids)} game IDs to {csv_path}")

if __name__ == "__main__":
    main()