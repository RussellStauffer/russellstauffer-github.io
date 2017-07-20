using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Web;

namespace MegaChallengeWar
{

    public class Deck
    {
        private List<Card> _deck;   // deck not public
        private Random _random;     // random not public

        private StringBuilder _sb;  // For testing only

        public Deck()
        {
            // Create Dealer's deck
            // declaring variables before sweep.

            _deck = new List<Card>();
            _random = new Random();
            _sb = new StringBuilder();

            string[] suits = new string[] {"Clubs", "Diamonds","Hearts",
           "Spades"};

            string[] kinds = new string[] {"2", "3","4", "5", "6", "7",
            "8","9","10","Jack","Queen", "King","Ace" };

            foreach (var suit in suits)
            {
                foreach (var kind in kinds)
                {
                    _deck.Add(new Card() { Suit = suit, Kind = kind });
                }
            }

        }

        public string Deal(Player player1, Player player2)
        {
            while (_deck.Count > 0)
            {
                // deal cards randomly to players

                dealCard(player1);
                dealCard(player2);
            }

            _sb.Append("<br/>All 52 Cards have been dealt.<br/>");

            // This section checks for the cards being dealt.
            // Remove this line after testing.

            return _sb.ToString();
        }

        private void dealCard(Player player)
        {
            // Randomly remove card from deck
            Card card = _deck.ElementAt(_random.Next(_deck.Count));

            player.Cards.Add(card); // add to players deck

            _deck.Remove(card); // removes card from dealers deck

            // This section checks that the players have been dealt 
            // all the cards. Remove on completing game.

            /*
            _sb.Append("<br/>");
            _sb.Append(player.Name);
            _sb.Append("has been dealt the ");
            _sb.Append(card.Kind);
            _sb.Append(" of ");
            _sb.Append(card.Suit);
            */
        }
    }
}

