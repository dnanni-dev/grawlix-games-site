const { chromium } = require('playwright'); const fs=require('fs');
const OUT='/home/claude/grawlix-games-site/brand/social/facebook/';
const css=fs.readFileSync('fontcss.css','utf8');
const logo='data:image/svg+xml;base64,'+fs.readFileSync('/home/claude/grawlix-games-site/brand/logo/holygrawlix-horizontal-light.svg').toString('base64');
const spark=(c,s,x,y)=>`<svg style="position:absolute;left:${x}px;top:${y}px;width:${s}px;height:${s}px;color:${c}" viewBox="0 0 7 7" fill="currentColor"><rect x="3" y="0" width="1" height="3"/><rect x="0" y="3" width="3" height="1"/><rect x="4" y="3" width="3" height="1"/><rect x="3" y="4" width="1" height="3"/></svg>`;
const html=`<style>${css}
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;overflow:hidden;position:relative;background:#F4F1EA}
.grid{position:absolute;inset:0;background-image:radial-gradient(rgba(11,11,16,.08) 2px,transparent 2.4px);background-size:28px 28px}
.panel{position:absolute;left:44px;top:44px;width:1104px;height:530px;background:#EBE5D7;border:6px solid #0B0B10;box-shadow:12px 12px 0 #0B0B10;transform:rotate(-1deg)}
.dots{position:absolute;inset:0;background-image:radial-gradient(rgba(47,85,212,.22) 2.6px,transparent 3.1px);background-size:22px 22px}
.narr{position:absolute;top:-6px;left:-6px;background:#FFD23F;border:6px solid #0B0B10;padding:14px 26px 10px;font-family:Bangers;font-size:42px;letter-spacing:.05em;line-height:1}
.logo{position:absolute;left:50%;top:54%;width:1000px;transform:translate(-50%,-50%) rotate(-1deg)}
.balloon{position:absolute;right:24px;top:96px;background:#fff;border:6px solid #0B0B10;border-radius:50%/44%;padding:16px 32px 12px;font-family:Bangers;font-size:42px;letter-spacing:.04em;line-height:1;transform:rotate(-3deg)}
.balloon::after{content:"";position:absolute;left:24%;bottom:-38px;width:42px;height:42px;background:#fff;border-right:6px solid #0B0B10;border-bottom:6px solid #0B0B10;transform:skewX(32deg) rotate(10deg)}
.url{position:absolute;right:28px;bottom:30px;background:#0B0B10;color:#FFD23F;padding:12px 26px 10px;font-family:'Space Grotesk';font-weight:700;font-size:44px;letter-spacing:.01em;line-height:1;transform:rotate(-1deg);box-shadow:6px 6px 0 #E8392E}
</style>
<div class="grid"></div>
<div class="panel"><div class="dots"></div>
 <div class="narr">MEANWHILE, AT A TINY INDIE STUDIO…</div>
 ${spark('#2F55D4',36,90,150)}${spark('#E8392E',44,60,430)}${spark('#0B0B10',40,1030,40)}
 <img class="logo" src="${logo}">
 <div class="url">holygrawlix.com</div>
 <div class="balloon">SOMETHING'S BREWING!</div>
</div>`;
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1200,height:630}}); await p.setContent(html); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400); await p.screenshot({path:OUT+'og-image-1200x630.png'});
await b.close();})();
