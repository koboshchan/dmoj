#pragma GCC optimize("Ofast")
#include <string.h>
#include <unistd.h>

#define ISZ (1 << 16)
#define OSZ (1 << 16)
char _i[ISZ], _o[OSZ], _ob[20]; int _ip, _op, _iend;

inline void __attribute__((constructor)) _c() { _iend = read(0, _i, ISZ); }
inline void __attribute__((destructor)) _d() { write(1, _o, _op); }
inline void ld() { if (_ip + 64 > _iend) { _iend -= _ip; memcpy(_i, _i + _ip, _iend); _iend += read(0, _i + _iend, ISZ - _iend); _ip = 0; } }
inline void fl() { if (_op + 64 > OSZ) { write(1, _o, _op); _op = 0; } }
template <typename T> inline void su(T &x) { char c; for (x = _i[_ip++] & 15; (c = _i[_ip++]) >= '0'; ) x = x * 10 + (c & 15); }
template <typename T> inline void si(T &x) { char c; bool neg = 0; if (_i[_ip] == '-') neg = 1, _ip++; for (x = _i[_ip++] & 15; (c = _i[_ip++]) >= '0'; ) x = x * 10 + (c & 15); if (neg) x = -x; }
inline void sc(char &c) { c = _i[_ip++]; }
template <typename T> inline void pu(T x) { int idx = 0; do _ob[idx++] = x % 10 | '0'; while (x /= 10); while (idx--) _o[_op++] = _ob[idx]; }
template <typename T> inline void pi(T x) { if (x < 0) { _o[_op++] = '-'; x = -x; } int idx = 0; do _ob[idx++] = x % 10 | '0'; while (x /= 10); while (idx--) _o[_op++] = _ob[idx]; }
inline void pc(char c) { _o[_op++] = c; }

// ld() — Loads the STDIN buffer in ISZ chunks if overflow; best used after any read operation.
// fl() — Flushes the STDOUT buffer in OSZ chunks if overflow; best used after any print operation.
// su() — Scans a single integer, assumed to be non-negative.
// si() — Scans a single integer, negative or positive.
// sc() — Scans a single character (does not skip whitespace).
// pu() — Outputs a single integer, assumed to be non-negative.
// pi() — Outputs a single integer, negative or positive.
// pc() — Outputs a single character.

// Source: https://dmoj.ca/user/Dingledooper