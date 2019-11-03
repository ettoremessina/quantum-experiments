// Etore Messina (c). All rights reserved.
// Licensed under the MIT License.

namespace ComputationalMindset.QuantumExperiments
{
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Measurement;

    operation RandomNumberGenerator() : (Result, Result, Result, Result, Result)
    {
        using (q = Qubit[5])
        {
            H(q[0]);
            H(q[1]);
            H(q[2]);
            H(q[3]);
            H(q[4]);

            let result = (M(q[0]), M(q[1]), M(q[2]), M(q[3]), M(q[4]));

            ResetAll(q);
            return result;
        }
    }
}
