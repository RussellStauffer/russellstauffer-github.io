using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Darts;

namespace ChallengeSimpleDarts
{
    public class Score
    {
        public static void ScoreDart(Player player, Dart dart)
        {
            int score = 0;

            if (dart.isTriple) score = dart.Score * 3;
            else if (dart.isDouble) score = dart.Score * 2;
            else score = dart.Score;

            // If both a triple and zero (bullseye) condition then
            // you score 50 points for an inner bullseye. Otherwise it
            // is scored as an outer bullseye worth 25 points;

            if (dart.isTriple && dart.Score == 0) score = 50;
            else if (dart.Score == 0) score = 25;

            player.Score += score;

        }
    }
}