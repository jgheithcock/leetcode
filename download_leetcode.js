// Add download button to leetcode problems
// Downloads source file with the problem base name, description, source code
// & test cases.


function addDownloadBtn() {
  const ideBtnBar = document.getElementById('ide-top-btns')
  const downloadBtn = document.getElementById('leet_download')
  if (ideBtnBar && !downloadBtn) {
    const title = getTitle()
    const btn = document.createElement("a");
    btn.id = 'leet_download';
    btn.style = "display: inline-block; margin-left:.25em;cursor:pointer;padding: 5px 8px;";
    btn.title = `Download Leetcode file for ${title}`;
    btn.className = "relative flex overflow-hidden rounded bg-fill-tertiary dark:bg-fill-tertiary";
    btn.innerText = "⬇️";
    btn.onclick = () => {
      const problemNum = title.split('.')[0].padStart(4, '0'); // e.g '0067'
      const baseName = document.URL.split('/')[4]
      const fileName = `${problemNum}-${baseName}.${fileExt()}`
      downloadFile(fileName, sourceCode());
    };
    ideBtnBar.appendChild(btn);
  }
}

addEventListener("DOMContentLoaded", (event) => {
	setTimeout(addDownloadBtn, 200);
});

function getTitle() {
  const titleEle = document.getElementsByClassName('text-title-large')[0]
  return titleEle.innerText
}

function getURL() {
  return document.URL
}

function getDifficulty() {
  // Easier to go up to common parent from title, then down to difficulty tag
  const titleEle = document.getElementsByClassName('text-title-large')[0]
  const commonParent = titleEle.parentElement.parentElement.parentElement
  return commonParent.children[1].children[0].innerText
}

function getInput(str) {
  const params = str.trim().split(', ')
  return params.map((p) => JSON.parse(p.split(' = ')[1]))
}

function getOutput(str) {
  return JSON.parse(str.trim())
}

function getTestCases() {
  // returns array of [input, output], input is parsed to be an array
  // of parameters. E.g. a = "11", b = "1" => ["11", "1"]
  const descSelector = '[data-track-load="description_content"]'
  const desc = document.querySelector(descSelector);
  const preTags = Array.from(desc.getElementsByTagName('pre'));
  const testCases = preTags.map((pre) => [
    getInput(pre.childNodes[1].textContent), 
    getOutput(pre.childNodes[3].textContent)
  ]);
  const header = "TEST_CASES = [\n";
  const footer = "\n]\n";
  const tab = "    "; // four spaces
  const cases = testCases.map((test) => tab + JSON.stringify(test))
  return header + cases.join(',\n') + footer
}

function getDescription() {
  // includes tests and constraints
  const descSelector = '[data-track-load="description_content"]'
  const descRaw = document.querySelector(descSelector).innerText
  const desc = descRaw.replace(/[ ]/g, " ") // replace nbsp with spaces
  return wrapText(desc, 80);
}

function getLanguage() {
  const ed = document.getElementById('editor')
  return ed.getElementsByTagName('button')[0].innerText
}

function getBlockCommentTags() {
  const language = getLanguage()
  if (['Python', 'Python3'].includes(language)) {
    return ["'''", "'''"];
  }
  else {
    return ["/*", "*/"];
  }
}

function fileExt() {
  const language = getLanguage()
  if (['Python', 'Python3'].includes(language)) {
    return 'py';
  }
  else {
    return 'cpp';
  }
}

function codeHeader() {
  const language = getLanguage()
  if (['Python', 'Python3'].includes(language)) {
    return "from typing import List\n";
  }
  else {
    return "";
  }
}

function codeFooter() {
  const language = getLanguage()
  if (['Python', 'Python3'].includes(language)) {
    return "# Testing Code\nif __name__ == '__main__':\n" +
      "\tfrom testing import runTests\n" +
      "\trunTests(Solution, TEST_CASES)\n";
  }
  else {
    return "";
  }
}

function getCode() {
  // Note this only grabs lines displayed
  const ed_sel = '.monaco-editor-background .monaco-mouse-cursor-text'
  const ed = document.querySelector(ed_sel)
  const lines = Array.from(ed.children) // convert from HTMLCollection
  // lines are not sorted by order, sort by style.top
  lines.sort((a, b) => parseInt(a.style['top']) - parseInt(b.style['top']))
  const codeRaw = lines.map(l => l.innerText).join('\n')
  const code = codeRaw.replace(/[ ]/g, " "); // non-breaking spaces -> spaces
  return code
}

function sourceCode() {
  const [c1, c2] = getBlockCommentTags();
  const title = `Leetcode problem ${getTitle()}`;
  const url = getURL();
  const difficulty = `Difficulty: ${getDifficulty()}`;
  const desc = getDescription();
  const code = getCode();
  const tests = getTestCases();
  const header = `${c1}\n${title}\n${url}\n${difficulty}\n\n${desc}\n${c2}\n`;
  return `${header}\n${codeHeader()}\n${code}\n\n${tests}\n${codeFooter()}`
}

// Utility methods
function wrapText(text, maxChars) {
  if (!text) {
    return '';
  }

  let wrappedText = '';
  let currentLine = '';
  
  for (const line of text.split('\n')) {
    for (const word of line.split(' ')) {
      if (currentLine.length + word.length + 1 <= maxChars) {
        currentLine += (currentLine ? ' ' : '') + word;
      } else {
        wrappedText += currentLine + '\n';
        currentLine = word;
      }
    }
    wrappedText += currentLine + '\n';
    currentLine = '';
  }
  return wrappedText;
}

// e.g. downloadFile("sample.txt", "Some sample text.");
const downloadFile = (fileName, content) => {
  const link = document.createElement("a");
  const file = new Blob([content], { type: "text/plain" });
  link.href = URL.createObjectURL(file);
  link.download = fileName;
  link.click();
  URL.revokeObjectURL(link.href);
};
