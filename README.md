<p>Name: Rocketry Flight Post-Processor</p>
<p>Author: Kevin Connell</p>
<p>Purpose: To post-process altimeter data from collegiate-level rocketry experiments, specifically comparing flight performance with targeted performance metrics.</p>
<p>Inputs:
  <ul>
    <li>Pre-processed CSV file with time, altitude, and velocity data (raw from altimeter)</li>
    <li>Vehicle section masses</li>
  </ul>
</p>

<p>Outputs:
  <ul>
    <li>Targeted performance metrics, including:
      <ol>
        <li>Apogee</li>
        <li>Time to Apogee</li>
        <li>Maximum Velocity</li>
        <li>Drogue Parachute Descent Velocity</li>
        <li>Main Parachute Descent Velocity</li>
        <li>Ground Impact Velocity</li>
        <li>Total Flight Time</li>
        <li>Descent Time</li>
        <li>Maximum Vehicle Drift</li>
        <li>Maximum Kinetic Energy</li>
      </ol>    
    </li>
    <li>Statistical comparison to target performance metrics, including:
      <ol>
        <li>Absolute error of flight parameters</li>
        <li>Relative (percent) error of flight parameters </li>
      </ol>
    </li>
  </ul>
</p>
