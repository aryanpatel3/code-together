import { Box, Center, Link, Text, VStack } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import axios from "axios";
import { Link as ReachLink } from "react-router-dom";

export function Problems() {
  const [error, setError] = useState(false);
  const [problems, setProblems] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/problems").then((res) => {
      if (res.data.data.problems) {
        setProblems(res.data.data.problems);
      } else {
        setError(true);
      }
    }).catch(() => setError(true));
  });


  return (
    <Box py={8}>
      <Center>
        <Text fontSize={"3xl"} fontWeight={"bold"}>
          Problems
        </Text>
      </Center>
      <Center mt={4}>
        {error && (
          <Text fontSize={"xl"} color={"red.500"}>
            An error occurred. Please try again later.
          </Text>
        )}
      </Center>

      <VStack spacing={4} alignItems={"flex-start"}>
        {problems.map((problem, i) => {
          return (
            <Text key={i} fontSize={"xl"}>
              {i + 1}.{" "}
              <Link as={ReachLink} to={`/problems/${i + 1}`}>
                {problem.title}
              </Link>
            </Text>
          );
        })}
      </VStack>
    </Box>
  );
}
