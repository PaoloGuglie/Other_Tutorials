import React, { useState, useEffect } from 'react';

function DigitalClock()
{
  const [time, setTime] = useState(new Date());

  // Start a clock when the page is created and update it every second:
  useEffect(() => {
    const intervalId = setInterval(() => {
      setTime(new Date());
    }, 1000);

    // Stop the clock when un-mounted:
    return () => {
      clearInterval(intervalId);
    }
  }, []);

  function padZero(number)
  {
    return (number < 10 ? '0' : '') + number;
  }

  function formatTime()
  {
    // Using military time:
    let hours = time.getHours();
    const minutes = time.getMinutes();
    const seconds = time.getSeconds();
    const meridiem = hours >= 12 ? 'PM' : 'AM';

    hours = hours % 12 || 12;

    return `${hours}:${padZero(minutes)}:${padZero(seconds)} ${meridiem}`;
  }

  return(
    <div className='clock-container'>
      <div className='clock'>
        <span>{formatTime()}</span>
      </div>
    </div>
  );
}

export default DigitalClock