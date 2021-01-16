# -*- coding: utf-8 -*-
import pandas as pd
from typing import List, Tuple
from pathlib import Path

class Dataset:
    """ Dataset object for sentence prediction """
    def __init__(self, path: Path = "/Users/ugo/Documents/Projects/project-dwight/DWIGHT/data/raw/The-Office-Lines-V3.csv"):
        try:
            self.df = pd.read_csv(path, encoding="latin-1")
        except:
            raise FileNotFoundError

    def get_lines(self, char) -> List[str]:
        """Get list of lines for a given character"""
        lines = []
        for i, line in enumerate(self.df.loc[:, "line"]):
            if self.df.at[i, "speaker"] == char:
                lines.append(line)
        return lines

    def get_line_pairs(self, char) -> List[Tuple[str, str]]:
        """Get list of previous line + line for a given character"""
        lines = []
        for i, line in enumerate(self.df.loc[:, "line"]):
            if self.df.at[i, "speaker"] == char: 
                if i == 0:
                    continue
                # Check that the line before is in the same scene
                if self.df.at[i, "season"] == self.df.at[i-1, "season"] and self.df.at[i, "episode"] == self.df.at[i-1, "episode"] and self.df.at[i, "scene"] == self.df.at[i-1, "scene"]:
                    lines.append((self.df.at[i-1, "line"], self.df.at[i, "line"]))
        return lines
    
    def get_line_pairs_as_list(self, char) -> List[str]:
        """Get list of previous line + line for a given character"""
        lines = []
        for i, line in enumerate(self.df.loc[:, "line"]):
            if self.df.at[i, "speaker"] == char: 
                if i == 0:
                    continue
                # Check that the line before is in the same scene
                if self.df.at[i, "season"] == self.df.at[i-1, "season"] and self.df.at[i, "episode"] == self.df.at[i-1, "episode"] and self.df.at[i, "scene"] == self.df.at[i-1, "scene"]:
                    lines.append(self.df.at[i-1, "line"])
                    lines.append(self.df.at[i, "line"])
        return lines
