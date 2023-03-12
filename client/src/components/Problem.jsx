import { useEffect, useState } from "react";
import { Container } from "@chakra-ui/react";
import axios from "axios";
import { Editor } from "./Editor";

export function Problem() {
  const [data, setData] = useState({
    title: "",
    description: "",
    test_cases: [],
    code: "",
  });

  useEffect(() => {
    axios.get("http://localhost:8000/problem").then((res) => {
      setData(res.data);
    });
  }, []);

  return (
    <Container>
      {data.title}
      <div>{data.description}</div>
      Test Cases:
      <ul>
        {data.test_cases.map((testCase, i) => (
          <li key={i}>{testCase.input}</li>
        ))}
      </ul>
      <Editor />
    </Container>
  );
}
