const { chromium } = require('playwright'); const { spawn } = require('child_process'); const path=require('path'); const fs=require('fs');
(async()=>{
  const tl=process.argv[2], out=process.argv[3], T=JSON.parse(fs.readFileSync(tl,'utf8'));
  const fps=T.fps||24, frames=Math.ceil(T.duration*fps);
  const browser=await chromium.launch({args:['--allow-file-access-from-files']});
  const page=await browser.newPage({viewport:{width:T.w,height:T.h},deviceScaleFactor:1});
  await page.goto('http://127.0.0.1:8765/video/engine.html?tl='+path.basename(tl));
  await page.waitForFunction(()=>window.__ready,null,{timeout:60000});
  const ff=spawn('ffmpeg',['-loglevel','error','-y','-f','image2pipe','-framerate',String(fps),'-i','-','-i',T.audio,'-c:v','libx264','-pix_fmt','yuv420p','-preset','veryfast','-crf','19','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',out],{stdio:['pipe','inherit','inherit']});
  const t0=Date.now();
  for(let i=0;i<frames;i++){
    await page.evaluate(t=>window.__render(t),i/fps);
    const buf=await page.screenshot({type:'jpeg',quality:92});
    if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
    if(i%240===0) console.log(`frame ${i}/${frames} ${((Date.now()-t0)/1000).toFixed(0)}s`);
  }
  ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await browser.close(); console.log('done',out);
})();
