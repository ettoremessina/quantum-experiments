// Ettore Messina (c). All rights reserved.
// Licensed under the MIT License.

using Microsoft.Quantum.Simulation.Simulators;
using Microsoft.Quantum.Simulation.Core;
using System;
using System.Threading.Tasks;

namespace ComputationalMindset.QuantumExperiments
{
    class Program
    {
        static void Main(string[] args)
        {
            const int shots = 8192;
            int [] counters = new int[1 << 5];

            var qDevice = new QuantumSimulator(throwOnReleasingQubitsNotInZeroState: true);
            for (int i = 0; i < shots; ++i)
            {
                var (m0, m1, m2, m3, m4) = RandomNumberGenerator.Run(qDevice).Result;
                int rnd =
                      ((m0 == Result.One ? 1 : 0) << 0)
                    + ((m1 == Result.One ? 1 : 0) << 1)
                    + ((m2 == Result.One ? 1 : 0) << 2)
                    + ((m3 == Result.One ? 1 : 0) << 3)
                    + ((m4 == Result.One ? 1 : 0) << 4);
                counters[rnd]++;
            }

            Console.WriteLine($"Bits\tValue\tCounter\tPerc");
            for(int i = 0; i < counters.Length; ++i)
            {
                string binary = Convert.ToString(i, 2).PadLeft(5, '0');
                double perc = Math.Round((counters[i] * 100.0) / shots, 2);
                Console.WriteLine($"{binary}\t{i}\t{counters[i]}\t{perc}%");
            }
        }
    }
}
