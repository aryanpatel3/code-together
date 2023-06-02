import { Button, Box, HStack, Text } from "@chakra-ui/react";

export function TestCases({ handleRunClick, results, testCases }) {
  return (
    <Box p={4}>
      <HStack alignItems={"flex-start"}>
        {testCases?.map((testCase, i) => {
          return (
            <Box key={i} p={2}>
              <Text fontSize={"lg"} fontWeight={"bold"}>
                Test {i + 1}
              </Text>
              <Text>Input: "{testCase.input}"</Text>
              <Text>Expected Output: "{testCase.expected_output}"</Text>
              <Text color={results[i] && "green.500"}>Result: {results[i] === true ? "passed" : "fail"}</Text>
            </Box>
          );
        })}
      </HStack>
      <Button onClick={handleRunClick}>Run</Button>
    </Box>
  );
}
