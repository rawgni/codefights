func arithmeticExpression(A int, B int, C int) bool {
    return A+B == C || A-B == C || A*B == C || A*C == B || B*C == A
}
