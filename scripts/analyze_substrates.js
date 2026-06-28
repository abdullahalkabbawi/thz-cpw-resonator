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
            
            // convert to THz if in Hz
            if (f > 1e11) {
                f = f / 1e12;
            }
            
            if (f >= 0.4 && f <= 0.8) {
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

analyze('data/trench_50um_depth_v2_S21.csv', 'GaAs Substrate (50um trench)');
analyze('data/trench_50um_si_S21.csv', 'Si Substrate (50um trench)');
