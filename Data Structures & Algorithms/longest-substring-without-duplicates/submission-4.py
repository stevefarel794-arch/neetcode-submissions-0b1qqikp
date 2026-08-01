class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        caracteres_vus = set()
        gauche = 0
        sous_chaine_max = ""

        for droite in range(len(s)):
            while s[droite] in caracteres_vus:
                caracteres_vus.remove(s[gauche])
                gauche += 1

            caracteres_vus.add(s[droite])
            if (droite - gauche + 1) > len(sous_chaine_max):
                sous_chaine_max = s[gauche : droite + 1]

        return len(sous_chaine_max)