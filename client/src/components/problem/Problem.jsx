import { useEffect, useState } from "react";
import { AbsoluteCenter, CircularProgress, Flex } from "@chakra-ui/react";
import axios from "axios";
import { Header } from "./Header";
import { LeftSide } from "./LeftSide";
import { RightSide } from "./RightSide";

export function Problem() {
  const [isLoading, setIsLoading] = useState(true);
  const [data, setData] = useState({
    title: "",
    description: "",
    test_cases: [],
    code: "",
  });

  useEffect(() => {
    axios.get("http://localhost:8000/problem").then((res) => {
      setData(res.data);
      setIsLoading(false);
    });
  }, []);

  return (
    <Flex direction="column" h="100vh">
      <Header />
      {isLoading ? (
        <AbsoluteCenter p="4" axis="both">
          <CircularProgress isIndeterminate />
        </AbsoluteCenter>
      ) : (
        <>
          <Flex flex="1">
            <LeftSide data={data} />
            <RightSide data={data} />
          </Flex>
        </>
      )}
    </Flex>
  );
}
