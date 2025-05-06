import React from 'react';

class Test extends React.Component
{
  constructor(props)
  {
    super(props);

    this.state = {
      count: 0
    }
  }

  componentDidMount()
  // This method can be defined in a class-based component.
  // It will run when my component first mounts.
  // Mounting is when the component performs its first full render.
  // So this function runs as soon as my component is rendered in the screen.
  {
    console.log("Mounted!");
  }

  componentDidUpdate()
  // Not called for the initial render, but each time the component it's updated.
  {
    console.log("Updated!");
  }

  componentWillUnmount()
  // When the component is going to be destroyed. In this method I can perform a
  // cleanup operation.
  {
    console.log("Cleanup!");
  }

  clickedButton()
  {
    this.setState({
      count: this.state.count + 1
    })
  }

  clickedDestroyButton()
  {
    this.props.setShowTest(false);
  }

  render()
  {
    return(
      <div>
        <p>Clicked: {this.state.count}</p>
        <button className='btn btn-primary'
        onClick={() => this.clickedButton()}>Click</button>

        <br></br>
        <br></br>

        <button className='btn btn-primary'
        onClick={() => this.clickedDestroyButton()}>Destroy me!</button>
      </div>
    );
  }
}

export default Test;