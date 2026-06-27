const fs = require('fs');

function analyze(filePath, label) {
    const lines = fs.readFileSync(filePath, 'utf-8').split('\n');
    let freqs = [];
    let s21s = [];
    for (let line of lines) {
        if (line.trim() === '' || line.startsWith('f') || line.startsWith('#')) continue;
        const parts = line.split(',');
        if (parts.length >= 2) {
            let f = parseFloat(parts[0]);
            let y = parseFloat(parts[1]);
            if (f >= 0.5 && f <= 0.7) {
                freqs.push(f);
                s21s.push(y);
            }
        }
    }
    
    let maxIdx = 0;
    let maxVal = s21s[0];
    for (let i = 1; i < s21s.length; i++) {
        if (s21s[i] > maxVal) {
            maxVal = s21s[i];
            maxIdx = i;
        }
    }
    
    const f0 = freqs[maxIdx];
    const halfMax = maxVal / 2;
    
    let leftIdx = maxIdx;
    while (leftIdx > 0 && s21s[leftIdx] > halfMax) leftIdx--;
    let rightIdx = maxIdx;
    while (rightIdx < s21s.length - 1 && s21s[rightIdx] > halfMax) rightIdx++;
    
    const fLeft = freqs[leftIdx] + (halfMax - s21s[leftIdx]) / (s21s[leftIdx+1] - s21s[leftIdx]) * (freqs[leftIdx+1] - freqs[leftIdx]);
    const fRight = freqs[rightIdx-1] + (halfMax - s21s[rightIdx-1]) / (s21s[rightIdx] - s21s[rightIdx-1]) * (freqs[rightIdx] - freqs[rightIdx-1]);
    
    const deltaF = fRight - fLeft;
    const ql = f0 / deltaF;
    
    console.log(`--- ${label} ---`);
    console.log(`f0: ${f0.toFixed(4)} THz`);
    console.log(`Peak: ${maxVal.toFixed(4)}`);
    console.log(`Delta f: ${(deltaF*1000).toFixed(2)} GHz`);
    console.log(`QL: ${ql.toFixed(2)}\n`);
}

analyze('data/trench_30um_depth_3um_gap_S21.csv', '30 um Depth');
analyze('data/trench_3um_capacitor_gap.csv', '50 um Depth');
analyze('data/trench_70um_depth_3um_gap_S21.csv', '70 um Depth');
