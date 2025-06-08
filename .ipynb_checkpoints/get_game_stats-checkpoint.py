#!/usr/bin/env python3
import os
import csv
import json
import time

from sportsradar_client import (
    get_game_statistics,
    API_KEY,
    ACCESS_LEVEL,
    LANGUAGE,
    FORMAT,
)

def main(max_games=10, short_delay=1.0, backoff_delay=60.0):
    assets_dir = "assets"
    game_ids_csv = os.path.join(assets_dir, "game_ids.csv")
    if not os.path.exists(game_ids_csv):
        print(f"Game IDs file not found: {game_ids_csv}")
        return
    ids = []
    with open(game_ids_csv, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ids.append(row["game_id"])
    selected_ids = ids[:max_games]
    stats_list = []
    for gid in selected_ids:
        success = False
        while not success:
            try:
                game_json = get_game_statistics(
                    API_KEY, ACCESS_LEVEL, LANGUAGE, gid, FORMAT
                )
                success = True
            except Exception as e:
                if hasattr(e, "response") and getattr(e.response, "status_code", None) == 429:
                    print(f"→ Received 429 for game {gid}. Backing off {backoff_delay}s …")
                    time.sleep(backoff_delay)
                else:
                    print(f"→ Skipping game {gid} due to error: {e}")
                    success = True
                    game_json = None
        if game_json:
            stats_list.append(game_json)
        time.sleep(short_delay)
    os.makedirs(assets_dir, exist_ok=True)
    output_path = os.path.join(assets_dir, "game_stats.json")
    with open(output_path, "w") as f:
        json.dump(stats_list, f, indent=2)
    print(f"Wrote statistics for {len(stats_list)} games to {output_path}")

if __name__ == "__main__":
    main()