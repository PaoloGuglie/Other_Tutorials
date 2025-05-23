import React, { useState, useEffect, useRef } from 'react';

function StopWatch()
{
  const [isRunnig, setIsRunnig] = useState(false);
  const [elapsedTime, setPassedTime] = useState(0);
  const intervalIdRef = useRef(null);
  const startTimeRef = useRef(0);

  useEffect(() => {

    if (isRunnig)
    {
      intervalIdRef.current = setInterval(() => { 
        setPassedTime(Date.now() - startTimeRef.current)}, 10);
    }

    // Cleanup function
    return () => clearInterval(intervalIdRef.current);

  }, [isRunnig]);

  function start()
  {
    setIsRunnig(true);
    startTimeRef.current = Date.now() - elapsedTime;
  }

  function stop()
  {
    setIsRunnig(false);
  }

  function reset()
  {
    setPassedTime(0);
    setIsRunnig(false);
  }

  function formatTime()
  {
    let minutes = Math.floor(elapsedTime / (1000 * 60) % 60 );
    let seconds = Math.floor(elapsedTime / 1000 % 60);
    let milliseconds = Math.floor((elapsedTime % 1000) / 10);
 
    minutes = String(minutes).padStart(2, '0');
    seconds = String(seconds).padStart(2, '0');
    milliseconds = String(milliseconds).padStart(2, '0');

    return `${minutes}:${seconds}:${milliseconds}`;
  }
  
  return(<>
    <div className='stopwatch'>
      <div className='display'>{formatTime()}</div>
      <div className='controls'>
        <button className='start-button' onClick={start}>Start</button>
        <button className='stop-button' onClick={stop}>Stop</button>
        <button className='reset-button' onClick={reset}>Reset</button>
      </div>
    </div>
  </>);
}

export default StopWatch;