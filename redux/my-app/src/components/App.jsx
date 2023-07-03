import React from "react";
import "./styles.css";
import { useDispatch, useSelector } from "react-redux";
import { increment, decrement } from "../store/actions/index";

function App() {
    // const [count, setCount] = useState("0");

    const count = useSelector((state) => state.counter)
    const dispatch = useDispatch();
    // console.log(count);

    return (
        <div style={{
            textAlign: "center", fontSize: "2rem"
        }}>
            <h1>Hello -- {count}</ h1>
            <button onClick={() => dispatch(increment(100))}> + </button>
            <button onClick={() => dispatch(decrement(100))}> - </button>
        </div>
    )
}

export default App;