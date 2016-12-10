func tennisSet(score1 int, score2 int) bool {
    if score1 >= 5 && score2 >= 5 {
        return score1 != score2 && (score1 == 7 || score2 == 7)
    }
    return score1 == 6 || score2 == 6
}
