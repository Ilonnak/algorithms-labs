#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct { int u, v, w; } Edge;

typedef struct { int p, r; } Node;

int find(Node ds[], int x){
    if (ds[x].p != x) ds[x].p = find(ds, ds[x].p);
    return ds[x].p;
}
bool unite(Node ds[], int a, int b){
    a = find(ds, a); b = find(ds, b);
    if (a == b) return false;
    if (ds[a].r < ds[b].r) { int t=a; a=b; b=t; }
    ds[b].p = a;
    if (ds[a].r == ds[b].r) ds[a].r++;
    return true;
}

    int cmp_edge(const void *A, const void *B){
    const Edge *a = (const Edge*)A, *b = (const Edge*)B;
    if (a->w != b->w) return a->w - b->w;
    if (a->u != b->u) return a->u - b->u;
    return a->v - b->v;
}

int cmp_lex(const void *A, const void *B){
    const Edge *a = (const Edge*)A, *b = (const Edge*)B;
    int au = a->u, av = a->v; if (au > av) { int t=au; au=av; av=t; }
    int bu = b->u, bv = b->v; if (bu > bv) { int t=bu; bu=bv; bv=t; }
    if (au != bu) return au - bu;
    if (av != bv) return av - bv;
    return a->w - b->w;
}

int main(void){
    const int V = 8;

    Edge E[] = {
        {1,3,1},
        {5,4,1},
        {2,6,3},
        {1,2,4}, {1,4,4}, {3,8,4}, {5,7,4},
        {3,4,5}, {3,6,5}, {8,7,5},
        {6,7,6}, {2,5,7}
    };
    const int M = sizeof(E)/sizeof(E[0]);

    qsort(E, M, sizeof(Edge), cmp_edge);

    Node dsu[9]; 
    for (int i=1;i<=V;i++){ dsu[i].p = i; dsu[i].r = 0; }

    Edge mst[8]; int used = 0; int total = 0;

    printf("Chosen edges (Kruskal order):\n");
    for (int i=0;i<M && used < V-1;i++){
        if (unite(dsu, E[i].u, E[i].v)){
            mst[used++] = E[i];
            total += E[i].w;
            printf("%d - %d  w=%d\n", E[i].u, E[i].v, E[i].w);
        }
    }

    printf("\nTotal weight = %d\n", total);

    qsort(mst, used, sizeof(Edge), cmp_lex);
    printf("MST edges (sorted):\n");
    for (int i=0;i<used;i++){
        int a=mst[i].u, b=mst[i].v; if (a>b){int t=a;a=b;b=t;}
        printf("(%d-%d)=%d\n", a, b, mst[i].w);
    }
    return 0;
}
