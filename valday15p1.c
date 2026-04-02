// 30 / 100 WA

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int id;
    int count;
    int k;
    int used;
} Cage;

int is_princess(char *line) {
    int count = 0;
    char temp[1000];
    strcpy(temp, line);
    
    char *word = strtok(temp, " \t\n\r");
    while (word != NULL) {
        if (strcmp(word, "Princess") == 0) {
            count++;
        }
        word = strtok(NULL, " \t\n\r");
    }
    return (count == 1);
}

int main() {
    int P;
    if (scanf("%d", &P) != 1) return 0;
    getchar();

    int princess_flags[501];
    for (int i = 0; i < P; i++) {
        char line[1000];
        fgets(line, sizeof(line), stdin);
        princess_flags[i] = is_princess(line);
    }

    Cage cages[501];
    int G = 0;
    int i = 0;
    while (i < P) {
        if (princess_flags[i]) {
            int count = 0;
            while (i < P && princess_flags[i]) {
                count++;
                i++;
            }
            G++;
            cages[G-1].id = G;
            cages[G-1].count = count;
            cages[G-1].used = 0;
        } else {
            i++;
        }
    }

    for (int j = 0; j < G; j++) {
        scanf("%d", &cages[j].k);
    }

    int max_k = 0;
    for (int j = 0; j < G; j++) {
        if (cages[j].k > max_k) max_k = cages[j].k;
    }

    for (int time = 0; time < max_k; time++) {
        int best_idx = -1;

        for (int j = 0; j < G; j++) {
            if (!cages[j].used && cages[j].k > time) {
                if (best_idx == -1) {
                    best_idx = j;
                } else {
                    if (cages[j].k < cages[best_idx].k) {
                        best_idx = j;
                    } else if (cages[j].k == cages[best_idx].k) {
                        if (cages[j].count > cages[best_idx].count) {
                            best_idx = j;
                        } else if (cages[j].count == cages[best_idx].count) {
                            if (cages[j].id < cages[best_idx].id) {
                                best_idx = j;
                            }
                        }
                    }
                }
            }
        }

        if (best_idx != -1) {
            printf("%d\n", cages[best_idx].id);
            cages[best_idx].used = 1;
        }
    }

    return 0;
}