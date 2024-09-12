"use client";

import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Container,
  Typography,
  TextField,
  Button,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";

interface MedicationSKU {
  id: number;
  medication_name: string;
  dose: string;
  presentation: string;
  unit: string;
  countries: string;
}

interface FormData {
  medication_name: string;
  dose: string;
  presentation: string;
  unit: string;
  countries: string;
}

const MedicationSKUCatalogue: React.FC = () => {
  const [skus, setSkus] = useState<MedicationSKU[]>([]);
  const [formData, setFormData] = useState<FormData>({
    medication_name: "",
    dose: "",
    presentation: "",
    unit: "",
    countries: "",
  });
  const [editingId, setEditingId] = useState<number | null>(null);

  useEffect(() => {
    fetchSKUs();
  }, []);

  const fetchSKUs = async () => {
    try {
      const response = await axios.get<MedicationSKU[]>(
        "http://localhost:8000/api/skus/"
      );
      setSkus(response.data);
    } catch (error) {
      console.error("Error fetching SKUs:", error);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      if (editingId) {
        await axios.put(
          `http://localhost:8000/api/skus/${editingId}/`,
          formData
        );
      } else {
        await axios.post("http://localhost:8000/api/skus/", formData);
      }
      setFormData({
        medication_name: "",
        dose: "",
        presentation: "",
        unit: "",
        countries: "",
      });
      setEditingId(null);
      fetchSKUs();
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };

  const handleEdit = (sku: MedicationSKU) => {
    setFormData(sku);
    setEditingId(sku.id);
  };

  const handleDelete = async (id: number) => {
    try {
      await axios.delete(`http://localhost:8000/api/skus/${id}/`);
      fetchSKUs();
    } catch (error) {
      console.error("Error deleting SKU:", error);
    }
  };

  return (
    <Container maxWidth="md">
      <Typography variant="h4" component="h1" gutterBottom>
        Medication SKU Catalogue
      </Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          fullWidth
          margin="normal"
          name="medication_name"
          label="Medication Name"
          value={formData.medication_name}
          onChange={handleInputChange}
        />
        <TextField
          fullWidth
          margin="normal"
          name="dose"
          label="Dose"
          value={formData.dose}
          onChange={handleInputChange}
        />
        <TextField
          fullWidth
          margin="normal"
          name="presentation"
          label="Presentation"
          value={formData.presentation}
          onChange={handleInputChange}
        />
        <TextField
          fullWidth
          margin="normal"
          name="unit"
          label="Unit"
          value={formData.unit}
          onChange={handleInputChange}
        />
        <TextField
          fullWidth
          margin="normal"
          name="countries"
          label="Countries"
          value={formData.countries}
          onChange={handleInputChange}
        />
        <Button type="submit" variant="contained" color="primary">
          {editingId ? "Update" : "Add"} SKU
        </Button>
      </form>
      <List>
        {skus.map((sku) => (
          <ListItem key={sku.id}>
            <ListItemText
              primary={`${sku.medication_name} - ${sku.dose}`}
              secondary={`${sku.presentation} | ${sku.unit} | ${sku.countries}`}
            />
            <ListItemSecondaryAction>
              <IconButton
                edge="end"
                aria-label="edit"
                onClick={() => handleEdit(sku)}>
                <EditIcon />
              </IconButton>
              <IconButton
                edge="end"
                aria-label="delete"
                onClick={() => handleDelete(sku.id)}>
                <DeleteIcon />
              </IconButton>
            </ListItemSecondaryAction>
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default MedicationSKUCatalogue;
