using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Web;

namespace MegaChallengeWar
{
    public class Game
    {
        private Player _player1;
        private Player _player2;
        private List<Card> _bounty;

        private StringBuilder _sb; 

        public Game(string player1Name, string player2Name)
        {
            _player1 = new Player() { Name = player1Name };
            _player2 = new Player() { Name = player2Name };
            _bounty = new List<Card>();
        }

        public string Play()
        {
            Deck deck = new Deck();

            string result = deck.Deal(_player1, _player2);

            int round = 0;  // Counter for rounds played

            while (_player1.Cards.Count != 0 && _player2.Cards.Count != 0)
            {

                _sb = new StringBuilder();

                Card player1Card = getCard( _player1);
                result += evalCard(player1Card, _player1.Name);

                // result += _sb.ToString();

                Card player2Card = getCard(_player2);
                result += evalCard(player2Card, _player2.Name);

                // result += _sb.ToString();             

                performEvaluation(_player1, _player2, player1Card, player2Card);

                result += _sb;

                // Since war can go on infinitely, we will limit the game
                // to 20 rounds.

                round++;

                if (round > 20)
                {
                    break;
                }

            }

            // determine the winner

            result += determineWinner();
            return result;
        }

        private Card getCard(Player player)
        {
            Card card = player.Cards.ElementAt(0);
            player.Cards.Remove(card);
            _bounty.Add(card);
            return card;
        }

        private void performEvaluation(Player player1, Player player2,
            Card card1, Card card2)
        {
            if (card1.CardValue() > card2.CardValue())
            {
                // player1 Wins statement here

                _sb.Append("<br/>  Player 1 Wins! <br/>");

                 player1.Cards.AddRange(_bounty);
            }

            else if (card2.CardValue() > card1.CardValue())
            {
                // player2 wins statement here

                _sb.Append("<br/>  Player 2 Wins! <br/>");

                player2.Cards.AddRange(_bounty);
            }
            // place War Method Here

            else
            {
                gotWar(player1, player2, card1, card2);
            }

            _bounty.Clear(); // clear cards from bounty.

        }

        // War Function

        private void gotWar (Player player1, Player player2,
            Card card1, Card card2)
        {
            _sb.Append("<br/> WE HAVE WAR!");
            _sb.Append("<br/> Each player places 2 cards face down.");
            _sb.Append("<br/>The third card is played:");

            for (int i = 0; i < 3; i++)
            {
                card1 = getCard(player1);
                card2 = getCard(player2);
                // Insert visualization for bounty here in future version.
            }

            _sb.Append(evalCard(card1, player1.Name));
            _sb.Append(evalCard(card2, player2.Name));

            performEvaluation(player1, player2, card1, card2);

        }
        // End War Function

        private string determineWinner()
        {
            string result = "";
            if (_player1.Cards.Count > _player2.Cards.Count)
                result += "<br/><br/>Player 1 Wins";
            else if (_player2.Cards.Count > _player1.Cards.Count)
                result += "<br /><br/>Player 2 Wins";
            else
                result += "<br/>The game is a tie.";

            result += "<br/> Player 1: " + _player1.Cards.Count + 
                " Player 2: " + _player2.Cards.Count;


            return result;
        }

        private string evalCard(Card playerCard, string player)
        {
            string cardPlayed = String.Format("<br/> {0} has played the {1} of {2}",
                player, playerCard.Kind, playerCard.Suit);

            return cardPlayed;
        }

    }
}