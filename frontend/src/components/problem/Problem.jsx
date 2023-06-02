import { useEffect, useState } from "react";
import { AbsoluteCenter, CircularProgress, Flex } from "@chakra-ui/react";
import axios from "axios";
import { Header } from "./Header";
import { LeftSide } from "./LeftSide";
import { RightSide } from "./RightSide";
import { useParams } from "react-router-dom";

export function Problem() {
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const { id } = useParams();

  const [data, setData] = useState({
    title: "",
    description: "",
    test_cases: [],
    code: "",
  });

  useEffect(() => {
    axios
      .get(`http://localhost:8000/problems/${id}`)
      .then((res) => {
        setData(res.data.data);
        setIsLoading(false);
      })
      .catch((err) => {
        setError(err);
        setIsLoading(false);
      });
  }, [id]);

  if (error) {
    return (
      <Flex direction="column" h="100vh">
        <AbsoluteCenter axis={"both"}>
          Something went wrong. Refresh this page to try again.
        </AbsoluteCenter>
      </Flex>
    );
  }

  if (isLoading) {
    return (
      <Flex direction="column" h="100vh">
        <AbsoluteCenter p="4" axis="both">
          <CircularProgress isIndeterminate />
        </AbsoluteCenter>
      </Flex>
    );
  }

  return (
    <Flex direction="column" h="100vh">
      <Header />
      <Flex flex="1">
        <LeftSide data={data} />
        <RightSide data={data} id={id} />
      </Flex>
    </Flex>
  );
}
