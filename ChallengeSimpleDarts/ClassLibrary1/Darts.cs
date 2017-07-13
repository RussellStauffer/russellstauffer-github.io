using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Darts
{
    public class Dart
    {
        public int Score { get; set; }
        public bool isDouble { get; set; }
        public bool isTriple { get; set; }

        private Random _random;

        public Dart(Random random)
        {
            // random = new Random();
            _random = random;
        }

        public void Throw()
        {
            Score = _random.Next(0, 21);

            int multiplier = _random.Next(1, 101);
            if (multiplier > 95) isTriple = true;
            else if (multiplier > 90) isDouble = true;
        }
    }
}
