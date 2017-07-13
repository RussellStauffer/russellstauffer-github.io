using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Darts;

namespace ChallengeSimpleDarts
{
    public class Game
    {
        private Player _player1;
        private Player _player2;

        private Random _random;

        public Game(string player1Name, string player2Name)
        {
            // set the player names from the Default screen event

            _player1 = new Player();
            _player1.Name = player1Name;

            _player2 = new Player();
            _player2.Name = player2Name;

        }

        public string Play()
        {
            // Game play continues until one player has 300+ points

            while (_player1.Score < 300 && _player2.Score < 300)
            {
                playerRound(_player1);
                playerRound(_player2);
            }
            return gameResults();
        }


        private void playerRound(Player player)
        {
            // Throw 3 darts
            // check for rings or bullseyes

            for (int i = 0; i < 3; i++)
            {
                Dart dart = new Dart(_random);
                dart.Throw();
                Score.ScoreDart(player, dart);
            }
        }

        private string gameResults()
        {
            // Create the final tally and display the winner and
            // player scores.

            string finalTally = String.Format("{0}: {1}<br />",
                _player1.Name, _player1.Score);

            finalTally += String.Format("{0}: {1}<br />",
                _player2.Name, _player2.Score);

            // outcome line.
            finalTally += "Winner is: ";
            finalTally += (_player1.Score > _player2.Score ?
                _player1.Name : _player2.Name);

            return finalTally;
        }
    }
}