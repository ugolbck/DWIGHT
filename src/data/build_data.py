# -*- coding: utf-8 -*-
import pandas as pd
from typing import List, Tuple
from pathlib import Path

class Dataset:
    def __init__(self, path: Path = "data/raw/The-Office-Lines-V3.csv"):
        self.df = pd.read_csv(path, encoding="latin-1")

    def char_lines(self, df, char) -> List[str]:
        """Get list of lines for a given character"""
        lines = []
        for i, line in enumerate(df.loc[:, "line"]):
            if df.at[i, "speaker"] == char:
                lines.append(line)
        return lines

    def char_line_pairs(self, df, char) -> List[Tuple[str, str]]:
        """Get list of previous line + line for a given character"""
        lines = []
        for i, line in enumerate(df.loc[:, "line"]):
            if df.loc[i, "speaker"] == char: 
                if i == 0:
                    continue
                # Check that the line before is in the same scene
                if df.loc[i, "season"] == df.loc[i-1, "season"] and df.loc[i, "episode"] == df.loc[i-1, "episode"] and df.loc[i, "scene"] == df.loc[i-1, "scene"]:
                    lines.append((df.loc[i-1, "line"], df.loc[i, "line"]))
        return lines
