import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
import { Box, Divider, TablePagination, Typography } from "@mui/material";
import React, { ReactNode } from "react";
import { UsePaginationResult } from "src/hooks/use-pagination";

interface LayoutTabContentProps<T> {
  leftContent: ReactNode;
  rightContent: ReactNode;
  table: ReactNode;
  pagination: UsePaginationResult;
  data: T[];
  title?: string | null;
}

const LayoutTabContent = <T,>({
  leftContent,
  rightContent,
  table,
  pagination,
  data,
  title,
}: LayoutTabContentProps<T>) => {
  return (
    <>
      {title && (
        <>
          <Box sx={{ paddingBottom: 3, px:3 }}>
            <Typography variant="h6">
              {title}: {data.length}
            </Typography>
          </Box>
        </>
      )}
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 2,
          my: 2,
          mx: 3,
        }}
      >
        {leftContent}
        {rightContent}
      </Box>

      {table}
      <TablePagination
        component="div"
        {...pagination}
        rowsPerPageOptions={[5, 10, 25, 100]}
        sx={{
          position: "fixed",
          bottom: 0,
          right: 0,
          left: 0,
          bgcolor: "secondary.lightest",
          borderTop: "1px solid",
          borderColor: "divider",
        }}
      />
    </>
  );
};

export default LayoutTabContent;
