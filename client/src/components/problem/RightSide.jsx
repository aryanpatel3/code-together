import { Box, Flex } from "@chakra-ui/react";
import { Editor } from "./Editor";
import axios from "axios";
import { TestCases } from "./TestCases";
import { useCallback, useState } from "react";

export function RightSide({ data }) {
  const [results, setResults] = useState([]);
  const [code, setCode] = useState(data.code);
  const { test_cases: testCases } = data;

  const onCodeChange = useCallback((value) => {
    console.log("value:", value);
    setCode(value);
  }, []);

  const handleRunClick = async () => {
    const res = await axios.post("http://localhost:8000/code", { code: code });
    setResults(res.data.results);
    console.log(results);
  };

  return (
    <Box w="65%" borderLeft="1px" borderColor="gray.200">
      <Flex direction="column" height={"100%"}>
        <Box borderBottom="1px" borderColor="gray.200" flex="7">
          <Editor code={code} onCodeChange={onCodeChange} />
        </Box>
        <Box flex="3">
          <TestCases
            handleRunClick={handleRunClick}
            results={results}
            testCases={testCases}
          />
        </Box>
      </Flex>
    </Box>
  );
}
