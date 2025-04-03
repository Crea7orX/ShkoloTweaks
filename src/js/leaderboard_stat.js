

let RankStatsWidget = document.querySelector("body > div.page-container > div.page-content-wrapper > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div.portlet-body.stats-rank-portlet-body.clearfix")
RankStatsWidget.classList.add("centerFlex")

let ShkoloTweeksRank = RankStatsWidget.children[0].cloneNode(true)
ShkoloTweeksRank.children[1].children[0].innerHTML = chrome.i18n.getMessage("ShkoloTweeksRankTooltip")

ShkoloTweeksRank.children[0].children[1].innerHTML = chrome.i18n.getMessage("ShkoloTweeksRankLabal")
ShkoloTweeksRank.children[0].children[0].innerHTML = chrome.i18n.getMessage("Loading")

RankStatsWidget.appendChild(ShkoloTweeksRank)