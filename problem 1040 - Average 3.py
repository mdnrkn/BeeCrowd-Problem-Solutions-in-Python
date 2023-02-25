n1, n2, n3, n4 = map(float, input().split())

weighted_avg = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

print(f"Media: {weighted_avg:.1f}")

if weighted_avg >= 7.0:
    print("Aluno aprovado.")
elif weighted_avg < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam_score = float(input())
    final_avg = (weighted_avg + exam_score) / 2
    print(f"Nota do exame: {exam_score:.1f}")
    if final_avg >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {final_avg:.1f}")
